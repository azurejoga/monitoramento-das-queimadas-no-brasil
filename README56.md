# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f7b2802-872c-3299-b87c-74e286776096 | -10.87385 | -53.99924 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd8a46c0-d528-3316-873f-f9607fc08df5 | -7.06172 | -46.74449 | 2026-09-20 04:40:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9c5eaf0-3e08-357a-a688-fcd5d0e65d21 | -9.80879 | -48.33163 | 2026-09-20 04:40:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d3740d2-1266-34e3-b625-b349dbe02b7d | -10.47692 | -46.29715 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 894c65c3-e781-35ce-9360-68d3f71cb0a4 | -5.97443 | -55.36356 | 2026-09-20 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d5dc5f7-c76f-31e9-8acc-c9938cce6142 | -6.33097 | -55.2652 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f58106b-ea54-3204-9b0a-e6705a93137d | -11.85833 | -47.63044 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e306c51e-6db2-3721-960e-b5c07cf97bfb | -5.72622 | -53.45229 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ef2c2e4-23ef-3ef9-b886-f74ccbc9ff05 | -12.22981 | -50.15543 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 946068c7-31e5-359a-82e6-032b2a4bfe4a | -8.84946 | -44.92009 | 2026-09-20 04:40:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbb64aaa-f687-3505-9787-9aca8293834d | -13.02636 | -46.90605 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21544556-5ef0-32a1-b03c-5ddb5e4acb39 | -11.44515 | -45.34159 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0d442d2-dca0-3ca2-80c3-40f62479204f | -11.99724 | -50.0371 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d246fe79-c8bc-3e38-9501-5b75e11e4a99 | -7.77708 | -44.82761 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cce03fb3-76f4-310c-812c-b537bd027bbf | -6.98451 | -45.80642 | 2026-09-20 04:40:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9dfbf977-d0d7-3913-b9db-26be0a3522ac | -5.97852 | -57.77709 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91d30e53-78c9-38eb-88d4-29a63b9caee2 | -12.12247 | -47.03681 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c6377694-37dc-31d6-bc49-89731665525d | -6.45336 | -48.43698 | 2026-09-20 04:40:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fdc03eee-f7ef-3683-bc27-e12d077b9e54 | -5.75899 | -57.45018 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 783c482a-0186-3378-ac9e-03cb2533e5ec | -8.42525 | -54.72857 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5745e192-208f-3a29-976f-596b1b82341a | -6.00329 | -51.78548 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c14eb18-9697-3007-8e68-566cd1c94af9 | -8.07294 | -45.49237 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8378775-d673-3b63-aafd-e2beed98c8ea | -12.76567 | -52.85926 | 2026-09-20 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1dd5dcf-148d-347f-80f8-4cb5150199b6 | -7.73914 | -44.68405 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| da398541-049a-31e7-8dd0-170066501152 | -11.12823 | -54.02251 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| adf273ce-8154-3617-b63c-a64cf71719b5 | -10.3902 | -48.99531 | 2026-09-20 04:40:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b4c7f02-8d87-33e6-8dd7-eab61a9e40f5 | -10.23879 | -45.34795 | 2026-09-20 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a307f9e-de3d-3d87-bf3a-4cd21f081cd7 | -5.88895 | -53.64821 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66e324da-2cef-3d3e-a7b6-9722377d2323 | -8.76954 | -48.71954 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c214184a-e735-31ab-9663-3d760f1bacd0 | -7.56167 | -45.43364 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 622a093d-d905-3bd3-a2fa-6ebf50f04dba | -11.85775 | -47.65694 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7f2d25ee-6dae-384b-aaf6-00e2d7acc7f4 | -8.85343 | -45.94507 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ff6a643-62ea-366d-a879-601abaa93941 | -10.49016 | -46.28097 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c366ad8f-6c79-31a9-9cb2-3974c22f8006 | -9.18005 | -51.51662 | 2026-09-20 04:40:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5ae99ca-9d10-3a28-92d2-e4586933ae09 | -7.54092 | -45.42632 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 91f99ff6-cc1d-3f43-841c-17df7ed1e866 | -12.3793 | -47.00675 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f55ac4b-2185-39a7-8071-d75654daede3 | -10.49255 | -46.26479 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66188fa6-b496-33c1-bfb8-816a33ff93a7 | -8.61263 | -54.59214 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e26cc445-5f0e-3643-845e-debe90f0352e | -9.0489 | -48.75699 | 2026-09-20 04:40:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58b60ba4-9fa6-3114-aac8-dce520cc9ab4 | -10.87065 | -57.15554 | 2026-09-20 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d702a613-2bda-31ab-a77f-e439adacce8a | -11.38085 | -51.4041 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 646ca639-44cb-35bb-bb24-ce2d771bb148 | -9.02519 | -48.77812 | 2026-09-20 04:40:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38945ccd-3853-34a4-b590-903d5d6dd695 | -10.86701 | -56.18017 | 2026-09-20 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6d14bf33-efee-3006-a0e3-2be74921458d | -10.27163 | -50.26737 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 423ba4d5-3777-326c-9282-ff7dbf49ae6d | -7.02583 | -47.43697 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afe3030d-7e17-3cea-b2a1-ec6aa875aef0 | -5.85716 | -53.50478 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cac10ed5-2d51-3b74-80bc-f5cc748694c2 | -8.16278 | -54.75838 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 44b79bd1-92d0-3cb6-9aba-df8d909fb61f | -10.41727 | -48.91008 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cf7c3cb1-0295-352b-acdd-475a471d0378 | -12.13289 | -47.03845 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 63b86843-fadc-395c-b12a-f0a7469b5ac0 | -11.28719 | -41.99971 | 2026-09-20 04:40:00 | NOAA-20 | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 858e5b82-55ba-37f8-9572-71e26da55b10 | -11.49974 | -47.73381 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9e45100-4983-3ada-94f2-627110d548ba | -6.87177 | -45.9739 | 2026-09-20 04:40:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67c5a84c-d0d1-3a90-b068-475460c1ab61 | -9.81321 | -48.32518 | 2026-09-20 04:40:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 660b00de-3325-3c03-8f35-d74dc452cf33 | -11.03792 | -48.28862 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be2c0207-a142-3a38-927d-9039bc8266eb | -9.19655 | -60.75808 | 2026-09-20 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f6c720b-f96e-37af-bf5f-9ec41c128bf8 | -7.52077 | -46.24044 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42ee3763-90aa-363b-bdd4-a2891c1ea906 | -6.75856 | -47.883 | 2026-09-20 04:40:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf3ce4ec-0ced-3219-89b7-0567c3ce4513 | -10.86197 | -57.14773 | 2026-09-20 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eaea0d3d-c0c9-3948-857c-3e0951274170 | -5.20139 | -56.04515 | 2026-09-20 04:40:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83dd2848-9638-3592-9258-3d9034f95d02 | -9.25274 | -45.9323 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cffc4bbd-251d-3be6-93d6-34ecdc52df3b | -10.60251 | -46.52033 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9921d0ab-01d5-39c2-9b7d-f392a30f861c | -11.38805 | -51.42512 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec4c5d97-af05-3e3c-a6e7-02f2b79e7812 | -11.37804 | -51.39966 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30b42a97-f424-33a1-bc59-acff839fd6a6 | -11.78949 | -49.82822 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ae28b9b-be1d-3515-b942-0d9502794011 | -8.29998 | -46.86297 | 2026-09-20 04:40:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5da4c61-7d34-37a0-961f-bdfa312a6c78 | -10.18862 | -48.50713 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32f26864-b5a1-3227-824d-0219c1acfb86 | -11.85889 | -47.67224 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| db1beefa-dae4-32d8-b847-00b2c1e1a157 | -9.79661 | -48.32259 | 2026-09-20 04:40:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acaff516-6984-3e51-9c26-1f2618d6a5cd | -7.76408 | -44.83921 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eb9c92ce-17a7-33a0-856f-0876ef8d0732 | -12.75327 | -46.21751 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 05588560-f271-32af-b796-255f5f48aabe | -9.02076 | -48.74177 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa9c75d0-d10b-3fc4-8e3a-3ae962f1108b | -10.26944 | -50.25957 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f894057-79a9-3562-bd70-25771b55499c | -13.94731 | -47.83628 | 2026-09-20 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7287481d-2abf-368c-a746-bbe0fbf9532b | -13.25188 | -51.73801 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48e2b72c-4f02-3245-ba72-cbc9dcc4cfbb | -5.8397 | -53.55662 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c35b28b6-d60a-3516-8b93-ae0e4291a4d1 | -10.91598 | -53.96928 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86088230-b9f7-39b9-8c13-09d126454240 | -6.98349 | -49.79868 | 2026-09-20 04:40:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 628644b5-2c2f-3d53-ab5b-71d1a536bf85 | -12.99575 | -46.91834 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e07e706f-0a43-3dd4-88f7-755f9696a5a2 | -10.41535 | -48.33819 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 625735d1-bb30-32e5-9608-e6dfc60b7495 | -7.4276 | -44.74629 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 266ea1b8-0661-36b9-b4b6-573c651aa389 | -8.57663 | -47.29058 | 2026-09-20 04:40:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e20006b-77d1-34d4-908e-fa010f3a2470 | -8.17956 | -54.73954 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 8e1702c8-8a08-3c83-8a02-180d41783c95 | -11.09163 | -48.28983 | 2026-09-20 04:40:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64770240-712e-3c0e-b76a-4868d46ca37e | -8.16649 | -54.73715 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27cdb768-50cd-380b-bc4e-cdf1b1762498 | -8.33659 | -46.46665 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c30f69b-dced-389e-aa6e-1768a067ba1b | -7.58411 | -46.73512 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ef490f2-ba72-3aa4-a661-90a74e95f19e | -7.2143 | -44.18694 | 2026-09-20 04:40:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 53c9498a-ed57-3660-b8f7-779cb53bc3ab | -10.67139 | -50.70372 | 2026-09-20 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c1845ae-31ae-3c4a-af07-8dbec40129a1 | -7.16151 | -47.47942 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90822ff2-26c8-3ee7-8de9-afaab5982a31 | -6.09072 | -56.46885 | 2026-09-20 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2af75f1b-aa69-3a2f-8eb1-67c0cbfd56ff | -7.54743 | -45.43144 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0516dd28-5906-351a-ab48-e11c57b7118e | -9.92978 | -48.38351 | 2026-09-20 04:40:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3aa276c0-384d-3d6b-af73-aef9db15f0b1 | -9.82199 | -46.42673 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc2d9f9b-2ed2-3ae7-b3ff-6b613c275450 | -11.32402 | -47.27876 | 2026-09-20 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 147d0992-f3bf-387c-9d4a-a5835ddb86cb | -11.0977 | -54.03321 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 1fbc7928-f6b2-3c9c-b2af-62a593fed42a | -6.39242 | -54.88419 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0b00805-9eb4-3192-a380-443d7dda3a7d | -10.13036 | -45.5517 | 2026-09-20 04:40:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d4469194-bc1a-3e8e-8455-133bf14c832f | -9.79407 | -45.06602 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5243244b-299e-3fd4-aa73-beafd8fa8ee2 | -13.38832 | -49.47161 | 2026-09-20 04:40:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37da87af-ea4f-3749-85fa-c0eaf6d7250f | -10.39844 | -48.8996 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README57.md)
