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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29c369a4-ddb2-36be-9e7a-32aea12c9f2d | -10.42293 | -47.28413 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a68f977b-6e13-3baa-b984-e390c17b66ff | -6.01716 | -53.488 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d810dc30-a2da-30f7-a71a-98e3d1212ba7 | -9.69765 | -58.0906 | 2026-10-09 04:27:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8987297a-8227-3b2e-9042-8a5df1bcf527 | -8.73186 | -45.14188 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 45d19001-54bd-3d78-b0b6-def62d4ff7bd | -13.1849 | -54.35948 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 834ce8f4-888c-3d58-8bcf-7069f0b0ec4f | -11.27914 | -45.19656 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54d3dbee-ba01-395f-b2a1-2a1b15fc5fb1 | -9.03975 | -46.86056 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c899c82-275a-3653-8cce-b0887b218da1 | -8.97238 | -45.90958 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| aeab1266-d636-3dfe-b6c6-9d6ea1568200 | -13.16483 | -54.34701 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7cd73d7e-0f65-3512-902a-5ec0d0ca7f5e | -6.44877 | -55.04431 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b324d97a-6617-3213-922b-60f6c7fb02e7 | -11.11215 | -45.6815 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99bf634e-9ffe-3f7f-8e94-ac92b6713d1a | -11.07328 | -44.00827 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b9bddec0-9795-3b26-b160-42864cd7090b | -11.19388 | -45.31779 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dd53c5ef-6ca1-38fc-a6a3-f96c4d9623b9 | -8.73533 | -45.16509 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f5225a4-2d8d-3d34-9f1d-d5c8f72a76a0 | -11.01302 | -45.42818 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| a2424823-6625-3c73-9dd5-7e62e7eb847d | -8.32732 | -45.4546 | 2026-10-09 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 355122ed-432c-340a-8ad9-0f5618e7d7c9 | -8.9128 | -45.22237 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1bcebee8-5cfe-31c4-aa1d-5c0827cda4ec | -6.13041 | -55.6857 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4ef117b-4e5c-3876-9a12-8c9ce69f9b07 | -13.40935 | -43.73079 | 2026-10-09 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 47d6dfab-35eb-3ab0-bf58-4d40c6706460 | -10.99879 | -47.47681 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b19c1ee1-3285-39c7-ac54-e1a789d7c2d3 | -12.85011 | -50.57668 | 2026-10-09 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52704dd2-92f0-3800-b20f-df7482b5228d | -8.43569 | -47.02675 | 2026-10-09 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68c0cc3f-e1fc-399f-a37a-0aea9fbaa2a5 | -11.65761 | -43.68088 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e6915bbd-1295-32c2-9e44-225480b5e390 | -9.22879 | -45.6554 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e575db6b-d1a1-306c-aa93-dddce40934d6 | -6.38924 | -55.26142 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9acee08-cb46-3c87-be1b-806d1096d7bd | -9.30197 | -47.46789 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| be79ae18-6f20-3d0b-a097-0702ff15a780 | -10.88702 | -48.51001 | 2026-10-09 04:27:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07695b27-e268-3b9b-aa00-7706846bc49d | -6.45656 | -55.4903 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d6817f9-6e19-3c07-a658-ab9ff563ad02 | -9.46035 | -44.60458 | 2026-10-09 04:27:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7427dad1-c371-33e3-b2e1-9e0308996bcc | -11.6205 | -43.69936 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ea08de1d-0a5e-357b-ba6d-79abfef2fdb3 | -7.05315 | -45.43156 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57ea70c4-d411-3743-b613-fe5f36630021 | -11.25265 | -47.74698 | 2026-10-09 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2ee975e4-7bd0-3ba6-9efd-1c04a9f83301 | -9.69176 | -58.08953 | 2026-10-09 04:27:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9aa740e6-1fe8-35f5-8b13-6fca212f9ee0 | -11.85776 | -48.03207 | 2026-10-09 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c36e5958-c85c-346b-a8d6-cbd582decf2e | -6.25662 | -52.8652 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e922476-827b-3682-a08b-ab6ab3e26850 | -8.33603 | -49.12793 | 2026-10-09 04:27:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2969dc67-7f10-3419-a73e-9e1b4f885b05 | -13.16403 | -54.35129 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 31627b55-59c9-3f5b-a225-aa5703d0c155 | -7.40344 | -44.7651 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e8241b3-215f-3fd4-afdf-d12c1b6a07a1 | -13.20221 | -54.36269 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b35bc6f-0c95-3da4-b805-e61223023ef8 | -13.18922 | -54.36029 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d04749a-fa8c-3265-b928-ed117e0474ae | -8.29902 | -45.44685 | 2026-10-09 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 648b5d89-7c1a-30ae-ae34-668b0d787c55 | -11.6117 | -43.70756 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 34e66208-bd6b-337d-a8c5-3039afe7023d | -7.18473 | -52.62653 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1cec58b9-39af-351f-a1cd-0717fba63a2c | -8.16753 | -48.60595 | 2026-10-09 04:27:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 872277c3-cdcb-37e6-a887-313490e5eac1 | -7.31566 | -43.98029 | 2026-10-09 04:27:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b2997242-cb5c-3f5a-8a3b-c27c44afc7ff | -8.72846 | -45.14136 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e00bb171-f114-3f60-b63b-aef0bf2be7d7 | -13.27106 | -46.96363 | 2026-10-09 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6415b72b-2a8c-39e5-8b9f-3a2f21441d8e | -8.73756 | -45.15032 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8b9c0461-b576-3f1c-a3bd-ba80a24ba4e3 | -7.65341 | -45.37771 | 2026-10-09 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eda96c6b-4fa2-3a0f-b231-f501c72826e2 | -12.479 | -54.39702 | 2026-10-09 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a644d710-4d45-35da-8c49-180b6f34d0b1 | -10.74446 | -46.61424 | 2026-10-09 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 352e272d-8bd4-3fba-bb2f-950f93c178d6 | -11.09351 | -43.99787 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 80727105-2241-3074-a2d5-3c0f13a69e26 | -6.45331 | -55.04835 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 420b09d3-f640-3918-ac2b-b8dba94238ac | -8.98897 | -47.53512 | 2026-10-09 04:27:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6e710f1-964b-380b-a018-432f5a110e7f | -7.75546 | -54.94767 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6ec26714-05ef-3891-ad0c-e35707acc3a6 | -8.20313 | -46.42215 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eeec9a56-e308-3489-a295-8450483b90ef | -14.08275 | -43.78125 | 2026-10-09 04:27:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0213ca0a-4296-3543-a747-0739c16b6486 | -8.96794 | -45.91623 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7d556e71-014f-309d-887b-b5b51efb8f73 | -7.48737 | -42.83417 | 2026-10-09 04:27:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1a0b7f0b-bc2c-3193-8af4-ce9535052f1b | -12.22464 | -57.10206 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 0d28b920-93a9-3dc6-ae3a-3d5de817486c | -11.67226 | -46.7712 | 2026-10-09 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5e93f6f-0584-3640-affe-cd381c6bd8f8 | -13.19788 | -54.36193 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b235b0b-9bd4-33e5-9e93-02eec1ee470d | -12.21412 | -57.12789 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b34c10b7-97f8-3fca-a0eb-7cd166a65078 | -11.22204 | -45.31833 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 431149f4-4f83-3c84-8bb3-e2fae27b6180 | -8.33208 | -45.02535 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e85b31bd-14d1-317d-8d79-503566c9c376 | -6.10388 | -53.50426 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 341ed078-f59d-3a82-a62b-77f22de216b1 | -6.72794 | -48.116 | 2026-10-09 04:27:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9998930b-13e0-3b84-a0f4-7a1a81526ed3 | -7.41708 | -44.76723 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1a48006-d3ce-34b9-a62e-15369c87068e | -9.27662 | -47.43536 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d7f4254-8db7-3234-80ba-9d441380e9d7 | -8.90664 | -45.24032 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2ffec1c-2dd1-3639-a508-6c9b434d00c1 | -9.04359 | -46.85761 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a23ad0c-aad3-36cd-a32b-a76a038233f9 | -8.97132 | -47.53595 | 2026-10-09 04:27:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6f3dd24-141e-3aa6-bba7-22edb78bfcaa | -10.93972 | -45.37773 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0722f8fa-c834-3301-b9ca-6e87d9b9c2c5 | -12.19779 | -57.13419 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b22fb6a3-d3a1-3a7d-b508-600be8e20cd2 | -9.2542 | -60.87918 | 2026-10-09 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21d0f5bf-c335-3cf8-8edd-3aad44f50e6e | -8.7398 | -45.13546 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7facb014-2bbe-3562-8899-a0f82cbf6331 | -11.77742 | -45.56417 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c65c9a2d-4961-39df-b7e2-548ba4fb4e1f | -11.31526 | -44.8333 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 829e7af0-0144-3b52-87f3-7c75cc0c695e | -9.03372 | -44.38216 | 2026-10-09 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d55f40a9-c365-3899-a274-6275278afdff | -10.39142 | -46.25391 | 2026-10-09 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c337a86-a79c-3245-ab63-f65c50f52d0f | -13.87526 | -43.80167 | 2026-10-09 04:27:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8429a1d-0735-34f7-b7f4-7631858ccdac | -8.94431 | -45.12844 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37807c63-bfdd-30a0-bb05-bd965b19734b | -13.19276 | -54.36542 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 58d42f12-7838-39b9-9c42-fb3767cba3f3 | -11.00208 | -47.47733 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e23ae29-35b4-3591-8941-d8c70e9237cf | -6.44367 | -55.04345 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07772b87-64c0-3ba5-bc2b-14d07b1a0bbf | -9.09686 | -59.39677 | 2026-10-09 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e421e55-e784-3cf4-90f2-3e7a3279bf80 | -8.1995 | -46.33607 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49229960-f0d4-3b4f-9b4e-ac894105d982 | -12.53887 | -46.52315 | 2026-10-09 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c30c87c-fe98-3fb2-b491-85120f98af55 | -7.47545 | -42.83713 | 2026-10-09 04:27:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 68290aea-9b60-35ff-bb0a-3822dddaf0db | -8.17955 | -49.5533 | 2026-10-09 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a5cea62-3b9e-394e-8e3c-e4ac48ac6485 | -11.74497 | -43.63826 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 508e3350-ea02-3c0d-ae48-3cd3b7b93ae8 | -11.76764 | -58.28439 | 2026-10-09 04:27:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 227d07da-5f11-319d-b17b-f908aa3ac3b3 | -10.06753 | -45.70135 | 2026-10-09 04:27:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf57411b-621b-335e-b4f8-ce18a290e349 | -10.92849 | -45.38474 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac17ca97-0490-3235-9aed-bcd9a50a3723 | -6.21703 | -52.88533 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4f5c029e-9231-3e2d-90cc-65c3d2fa3f19 | -7.4554 | -42.84335 | 2026-10-09 04:27:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 534f6412-1de1-3921-9943-4ae7c0a6150c | -12.22585 | -57.10152 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| e72a53b0-f8b0-3a47-8832-d4f6026ea8b6 | -9.29694 | -47.41365 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ed8c961-a4a3-3e35-a3f7-4152a66acc36 | -8.49181 | -54.63545 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f627d4ec-7949-3fd6-952e-20baa669c20e | -9.84491 | -47.47711 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README104.md)
