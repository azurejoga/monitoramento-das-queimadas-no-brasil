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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6518fd7-a7d1-3e3a-aa34-18044aa6ea4d | -10.97443 | -47.40239 | 2025-07-30 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d2a3a0b2-795b-3f7e-937c-ac17753f9535 | -12.26521 | -47.00358 | 2025-07-30 04:29:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10e69a21-3e37-3a55-af7b-cfc7f8cf723c | -12.61567 | -48.06434 | 2025-07-30 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 55f50ddf-f97d-38f2-b54f-fabc0a84f15b | -12.8203 | -45.44398 | 2025-07-30 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3837c262-20b1-35ba-ac09-0ed4e6fa83e4 | -12.80931 | -45.44622 | 2025-07-30 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1c607905-84f9-3463-9703-a9fd471b0fa2 | -12.0647 | -40.00934 | 2025-07-30 04:29:00 | NPP-375D | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 260f12be-5462-376e-bddc-6c822c3c1368 | -9.4616 | -57.85123 | 2025-07-30 04:29:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3a260828-8993-3407-9dde-59dfdce4d46b | -11.57014 | -47.89322 | 2025-07-30 04:29:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc778a7f-6419-39f5-9f03-1e4460d8da87 | -10.94151 | -45.78931 | 2025-07-30 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fea99bf-4945-39ae-b242-e69ee6a71ed8 | -11.32065 | -48.91521 | 2025-07-30 04:29:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b69a4944-aaae-35b4-9529-2b77ec86dce5 | -11.37683 | -49.00082 | 2025-07-30 04:29:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d18ffd9-9938-30a8-9713-4073c3878609 | -10.82197 | -49.37787 | 2025-07-30 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d8d5660-dab7-3474-98e2-71af29dd3feb | -13.3405 | -40.04753 | 2025-07-30 04:29:00 | NPP-375D | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 631ba3c1-fecb-3a57-a2a4-ad2b49ef9cc7 | -12.72746 | -47.012 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ab70cde-96ca-383f-8dae-2c292b436513 | -11.9727 | -46.68734 | 2025-07-30 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 565a404a-4990-3fce-8553-381bfc733bfa | -11.46926 | -45.11129 | 2025-07-30 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0eb4e79b-c55b-3f02-9fa7-87ea0642ce72 | -11.32404 | -48.91578 | 2025-07-30 04:29:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26c4fbad-0ea2-3d0c-9edc-f092672af627 | -11.46115 | -45.11797 | 2025-07-30 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a5d0841e-b64c-3b7e-89af-483e8938b7bc | -11.34529 | -51.24907 | 2025-07-30 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 144c4e90-187d-3596-b609-ceb3bc320f92 | -11.34608 | -51.24449 | 2025-07-30 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2e1896c-025b-378a-9e82-ecf95dbab094 | -11.32564 | -48.9274 | 2025-07-30 04:29:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e0a7a46-596c-3994-a3af-f1641f4a33a2 | -12.14987 | -44.76832 | 2025-07-30 04:29:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91252dce-3a80-31e5-834d-d0ef6e5078ea | -11.99015 | -46.92687 | 2025-07-30 04:29:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fa96a81-f683-343d-952b-cdb29237620f | -12.95129 | -46.89767 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eec95db5-eaf6-3272-b41a-fa7d01ae6fda | -12.81278 | -45.44676 | 2025-07-30 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aefc1341-3000-34a6-9247-84c1db11b2c9 | -11.9214 | -44.54384 | 2025-07-30 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d448f12e-d758-333c-83e3-d11134533303 | -11.27461 | -52.47163 | 2025-07-30 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 864d424c-8f9b-3b02-9170-80b8b4e05903 | -11.92497 | -44.54438 | 2025-07-30 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f80eb767-ad8d-37b9-b9f4-3741e5561d3c | -10.70789 | -48.8568 | 2025-07-30 04:29:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cd80bb38-7e6e-3c6d-b22e-be1ffb1c31db | -11.98295 | -46.95114 | 2025-07-30 04:29:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49d41bc2-d22d-35a1-bb80-710de1ec69d4 | -11.32684 | -48.92004 | 2025-07-30 04:29:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba5e3619-8371-3a70-a3c2-37ee6703c99c | -12.5452 | -44.72821 | 2025-07-30 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7641346b-a312-314b-ab97-cc0bff75c028 | -11.31519 | -49.95623 | 2025-07-30 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7a5b015-2182-3034-aae0-11bf03074173 | -10.93925 | -45.78144 | 2025-07-30 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6ed13fa-278f-3853-bfea-0d917964413d | -11.92201 | -44.53971 | 2025-07-30 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6aa0be1-22cd-31eb-93b9-39105edf7163 | -12.54877 | -44.72876 | 2025-07-30 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 681d5f00-7766-3617-9862-7acd35912a5c | -12.54816 | -44.73287 | 2025-07-30 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f11ffeb6-5102-3e17-8db6-2d9a695cd3de | -11.99164 | -46.69764 | 2025-07-30 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc5d884b-3a2a-3a3b-b9cd-6b147eacdd7d | -12.80989 | -45.44234 | 2025-07-30 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9599e5ca-4856-3425-a18a-62f9e5ab4fff | -11.46173 | -45.11412 | 2025-07-30 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| c612ae1a-c3fe-3e55-b621-7a027bbcb993 | -12.619 | -48.06489 | 2025-07-30 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a292922d-dc8c-3083-ae68-1ea9094b4608 | -10.7107 | -48.86108 | 2025-07-30 04:29:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd4872ef-a85e-3818-a66a-285e8f7def11 | -10.72594 | -50.4325 | 2025-07-30 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5053bb5-a958-32a9-b906-3e3eee1af7f0 | -12.4737 | -47.27271 | 2025-07-30 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 321a5d3e-681c-30ad-8747-d07ccfa969c7 | -12.95462 | -46.89823 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d9ce0bb-8625-3091-b3d8-eb3fcbf417dc | -12.26576 | -47.00003 | 2025-07-30 04:29:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 28f6063d-fe6f-3aff-aef8-c3c71e037aa8 | -12.47979 | -47.27732 | 2025-07-30 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe8fd471-f75d-3d96-96d8-ae3258297123 | -12.47592 | -47.28032 | 2025-07-30 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e7a5eb31-c310-36db-a647-bc8525759aeb | -12.47647 | -47.27679 | 2025-07-30 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0923218b-88e0-3868-a65a-f77b2f55d3cd | -10.93869 | -45.7851 | 2025-07-30 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ade6da9-2ab2-30ff-874b-49e81d86a1a9 | -12.05738 | -48.77344 | 2025-07-30 04:29:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08806851-288c-3fc3-8015-a2fc5376b693 | -11.98885 | -46.69355 | 2025-07-30 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d1a335f-e08e-3402-98dc-2fa67b558844 | -12.81394 | -45.439 | 2025-07-30 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d497ceee-de0d-30cd-acfc-71f4a80f6a82 | -11.98496 | -46.69658 | 2025-07-30 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72584796-ea8b-3f58-b823-eba5e0c47538 | -12.70717 | -47.78903 | 2025-07-30 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0555c741-7caf-35f0-96fa-4a4b8685e188 | -12.81892 | -43.09313 | 2025-07-30 04:29:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 554cb1c0-cb69-3b4e-a018-6fe03e661954 | -12.7291 | -47.00143 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7f8e1d0-d833-3868-87d9-c84f80a54eff | -11.98162 | -46.69605 | 2025-07-30 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 154f1be6-bb72-3bbe-a488-04e58f43d103 | -11.81341 | -44.26825 | 2025-07-30 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d7cf330-5925-3de6-97a9-efe44603d81e | -12.26909 | -47.00056 | 2025-07-30 04:29:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 23bc9d5c-4d15-3de4-b86e-8711c38201a4 | -11.97604 | -46.68786 | 2025-07-30 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b42d8e4-540e-3534-a044-1c9cb14e66fc | -10.7113 | -48.85737 | 2025-07-30 04:29:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88f5e64a-75f7-3c7f-98ae-305dd088fcd3 | -11.46521 | -45.11464 | 2025-07-30 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| e7bf56f5-2c3c-384b-a0a4-f251be6cb0fe | -10.69988 | -48.86309 | 2025-07-30 04:29:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fc0c7a71-5d87-3d09-be16-4fea97ba3231 | -12.81683 | -45.44343 | 2025-07-30 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a5b33409-8147-3fd5-be9b-98114db8d14a | -11.47216 | -45.11563 | 2025-07-30 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 782a0d0f-93c6-359c-add9-e1258c660dda | -10.70329 | -48.86365 | 2025-07-30 04:29:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44e643d5-66b4-3017-b426-233d28dac52d | -10.43784 | -48.3258 | 2025-07-30 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e6dd10d-2234-3fb2-ac3b-1ff866a13578 | -11.50129 | -48.38581 | 2025-07-30 04:29:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df20a46a-9d1a-39d8-9fd9-a587bcb3577b | -11.04705 | -44.78197 | 2025-07-30 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8e6de80-ba2e-37da-ac5e-4a2daa71e58a | -12.73188 | -47.0055 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 649f3723-a735-3ac9-bdf5-a6a33966eb02 | -11.98551 | -46.69302 | 2025-07-30 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19dfcf50-e60e-37b0-8c06-8f09d8c3e3d8 | -11.81527 | -44.25553 | 2025-07-30 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27db1cc9-c01e-3e67-9765-8eae1e9a4417 | -10.70729 | -48.86051 | 2025-07-30 04:29:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3f3624e8-0c8b-3bed-974b-edf1bcc6963f | -12.728 | -47.00849 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e09ec1f1-aea8-332d-aeeb-07eb88a65bfb | -11.34075 | -51.253 | 2025-07-30 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96dc6b1c-fb7a-32db-bfeb-69cfa68b081c | -11.45826 | -45.1136 | 2025-07-30 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| eb4e6469-d0df-30b0-8173-cd7fd6b5eb63 | -11.98995 | -46.68642 | 2025-07-30 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cc48faa-140f-3033-ae89-42c8a6052d86 | -11.34154 | -51.24841 | 2025-07-30 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 831d3ecc-c48c-3ecd-91ec-c71f5d83bc43 | -12.47703 | -47.27325 | 2025-07-30 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9e33e213-ed22-3cce-8643-08771cde20e0 | -9.45888 | -57.85386 | 2025-07-30 04:29:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3f7bfe47-e11c-36f6-ba1a-c398f082438a | -11.98239 | -46.95468 | 2025-07-30 04:29:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce3dc99b-8258-32ce-bf25-9ba194cd5c83 | -12.95797 | -46.89874 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a859f5b2-dc97-378a-b62f-b134c358ce91 | -12.72855 | -47.00497 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7f2a19d8-632d-3ea3-a257-0a14fd9d3f80 | -12.73134 | -47.00901 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff9d09f6-6f1b-3df0-a3de-f8e84d5ee8d9 | -12.70661 | -47.79256 | 2025-07-30 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2521aaaf-a264-3f6a-a776-8a4a5e1e02a1 | -11.53472 | -44.26531 | 2025-07-30 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09da03c0-6450-3896-876f-d4a53838d047 | -10.94207 | -45.78565 | 2025-07-30 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fc55d9b-9e04-3791-a9ce-17be397867e3 | -11.27865 | -52.4724 | 2025-07-30 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f82688f7-4f98-3f4b-b10f-143c5c76942f | -11.53535 | -44.26111 | 2025-07-30 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18de651f-7531-3282-a03a-72bf72254fae | -12.81336 | -45.44288 | 2025-07-30 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5f760266-36f9-3639-b4c5-a9c56540a86b | -10.82543 | -49.37846 | 2025-07-30 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc5662c8-d49f-353a-a8cb-f289b22cc120 | -12.48035 | -47.27379 | 2025-07-30 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1f4585e-c194-346c-9c2a-6bf8ab29b87c | -11.98382 | -46.68181 | 2025-07-30 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df61ae60-4e74-3fee-88bb-c3ce0addd2ef | -11.9883 | -46.69712 | 2025-07-30 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f90022be-d0a0-3ce8-b5f8-dc92c2508db8 | -11.81827 | -44.26033 | 2025-07-30 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46d015da-d8c8-34f6-8deb-69e60fb0f1c9 | -10.94377 | -45.79717 | 2025-07-30 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8820239-cae2-3d6e-8e9c-bfce628bf504 | -12.46012 | -44.08763 | 2025-07-30 04:29:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3863f670-c1d3-3fb7-8c8b-fcd06716cba1 | -11.34451 | -51.25366 | 2025-07-30 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02fc55ad-17d5-3ed9-84f0-0e30667f9ead | -11.32005 | -48.91889 | 2025-07-30 04:29:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |


[Clique aqui para ver as próximas entradas](README25.md)
