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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c847bac-f748-3d8c-a594-cd91ca271495 | -13.29302 | -47.58075 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5ba0b306-c1d0-3514-bf7f-ee866c43a818 | -9.48342 | -49.8324 | 2025-10-05 00:33:00 | TERRA_M-M | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 546b3170-faf2-3454-9004-a7104b51ec90 | -15.54416 | -46.8026 | 2025-10-05 00:33:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a446d238-141e-39b6-a167-04be93d0a2d1 | -12.29146 | -49.21268 | 2025-10-05 00:33:00 | TERRA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7cac4bf0-1971-3098-8eec-9abd258aaa1d | -16.60916 | -49.3766 | 2025-10-05 00:33:00 | TERRA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 248a6a9d-7030-3fc2-a034-1e05c2e2960c | -13.7302 | -51.27169 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fab3990a-b32f-3117-a27e-1032264ae949 | -14.93354 | -46.92053 | 2025-10-05 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2f35dafe-c411-3dc4-9a63-d6d20d390046 | -15.38869 | -47.94876 | 2025-10-05 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 2d7a48d7-2679-351f-9c47-391738dc13e1 | -15.13482 | -45.75907 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 8e511c93-e06a-377b-aace-4356376e427e | -14.66097 | -48.34781 | 2025-10-05 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 789e7f73-2274-3935-9121-8b10df464f97 | -12.127 | -49.42887 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2aafdfb7-7836-32d1-9708-a66ffd272366 | -11.09949 | -49.86839 | 2025-10-05 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4591d7ce-d47e-34c8-8922-7377b4616c8f | -10.72048 | -44.18185 | 2025-10-05 00:33:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b993f35c-0530-35b6-a89e-cc6f53008e3e | -15.59008 | -52.51027 | 2025-10-05 00:33:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 29.7 |
| dd66d479-11f0-38a5-88df-399e7f413925 | -11.81366 | -48.88084 | 2025-10-05 00:33:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b1c505fa-3633-3e47-89ae-da37c918f026 | -11.13819 | -47.9269 | 2025-10-05 00:33:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e3798c7e-d585-36bc-8f4e-a0ac0ec74454 | -13.71245 | -47.34954 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b2fab838-e2ab-3708-b082-477cb5b1041e | -11.71984 | -45.35689 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 43a92868-a87d-320a-b456-bb5e58ec23fa | -15.29796 | -47.95917 | 2025-10-05 00:33:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| db76ebeb-f0af-31cf-bf53-4cb734f9fdc0 | -12.97193 | -50.99759 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a6c7aa84-a687-39d4-9392-b70cf12ba8e1 | -11.11623 | -47.18279 | 2025-10-05 00:33:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 38c63bcb-7ad9-33c2-9e1a-c0e6f56a04bd | -11.62086 | -47.74579 | 2025-10-05 00:33:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dd42788f-9bf6-3d15-ae5b-fda03bc3fb1f | -8.59945 | -46.29249 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 721adfe5-e3e1-3df2-a443-451384a19a05 | -10.93548 | -47.07991 | 2025-10-05 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f88982b7-1d0d-3927-8d24-93532e928704 | -12.89838 | -47.33163 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fcf3cca6-3461-3744-8ddb-67e81f059866 | -10.45751 | -47.80408 | 2025-10-05 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| dc7a79dd-2759-38c3-bf28-cc674538cd4a | -12.12825 | -49.43827 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 643d63fe-1460-3794-bfe5-8f8ca7751b94 | -12.77194 | -48.82172 | 2025-10-05 00:33:00 | TERRA_M-M | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| e771d7e1-9b7c-3843-8a66-93bca18c6914 | -15.12136 | -45.73111 | 2025-10-05 00:33:00 | TERRA_M-M | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8aebd9a0-ebd3-357b-b26e-c6312d3ce1b7 | -12.97761 | -51.04325 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 90933957-6b9f-3459-9a96-b211e04e8a72 | -13.92197 | -48.19717 | 2025-10-05 00:33:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2cd2f409-1005-34f0-b86f-3bad33eec1b5 | -13.28042 | -47.6194 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1f279b84-f73f-3370-a650-af37d2b654cc | -16.35839 | -51.45582 | 2025-10-05 00:33:00 | TERRA_M-M | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 5da6ffb9-1eec-3cf7-815d-cc4ddac1811a | -13.31505 | -48.08018 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 3ddbe678-0fb8-35e1-b70a-888fcc7b407a | -11.80768 | -46.85859 | 2025-10-05 00:33:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 02fb93b1-f81e-39dc-9724-7e60500c14ad | -16.12327 | -53.99288 | 2025-10-05 00:33:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 01aed7b0-bdcd-3cbb-a207-bdbc55fac2bb | -13.14863 | -50.95652 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 6a955c69-19ab-3253-a30e-ba7eb962055d | -11.48851 | -45.03832 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 22218627-f6de-3c88-bd81-04ffb6c3c090 | -12.2825 | -49.21396 | 2025-10-05 00:33:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 6d735e17-3d10-3345-bf34-83d0d9c28c5d | -11.47863 | -45.04015 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 17076e7d-4b0c-3211-8ebd-c0760cedba98 | -9.86067 | -48.8134 | 2025-10-05 00:33:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 07d01e6a-4397-3a12-9b8f-c88dd7154825 | -15.57508 | -52.48112 | 2025-10-05 00:33:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 30cd0b60-6bd7-36dd-9950-23653530cbf8 | -13.28923 | -47.61808 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a549a785-0fff-34a5-8e6f-de1cbb99bc20 | -10.6419 | -46.31992 | 2025-10-05 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| f6a3001b-da38-3821-9522-79f0e4726a7c | -11.86369 | -56.85924 | 2025-10-05 00:33:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| bb202ca0-a82d-39a5-bbc6-aa0a81eb1c9d | -15.4293 | -47.57364 | 2025-10-05 00:33:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d54bf2e2-ab47-335d-a27b-f8bcbf7cd697 | -15.59964 | -52.49286 | 2025-10-05 00:33:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1c209cbd-72bb-3d2a-9282-c3c0294b83b6 | -13.38117 | -47.55245 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a8fae11f-e967-376f-b16c-cb569f6e5887 | -11.12019 | -47.21057 | 2025-10-05 00:33:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 52ef179c-4127-34d9-b1e9-8d7d4e7555ea | -13.30057 | -47.57036 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9eacdc0b-1e83-30c2-bda7-3bba19504434 | -15.75354 | -46.26943 | 2025-10-05 00:33:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a81564ee-e946-3620-808a-79afb996262f | -14.68657 | -48.26933 | 2025-10-05 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9cc2082e-1218-3c27-89da-8a1f80436f1a | -15.29879 | -46.31335 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f3b6bd90-e493-3df4-a015-3198182ce803 | -11.81946 | -45.05523 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 01992503-c3b6-3206-b6b0-42186906cfef | -15.38745 | -47.93964 | 2025-10-05 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f3247be1-381e-3a8b-a1f0-91ac0e39bc6c | -15.13193 | -45.73945 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 6bf33b70-b67c-3d07-8ece-772aadc6d2e4 | -10.19313 | -46.72959 | 2025-10-05 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e9bc1ffa-f871-3e60-9112-29f1858a8657 | -14.66983 | -48.3464 | 2025-10-05 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b74d9dc1-04c6-3304-84a5-f72af7c71b02 | -13.27791 | -47.60142 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 941d64be-3b55-32bd-aedb-761e5db8986a | -11.23023 | -47.79753 | 2025-10-05 00:33:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6bea9992-6049-37fc-bfb3-2761a6885f10 | -13.3504 | -48.05943 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c43a514a-ceb2-313b-87a0-d58bf41f04fc | -11.24665 | -47.78603 | 2025-10-05 00:33:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c06ae902-0120-317d-ba27-04be1804037d | -12.56277 | -48.16587 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| ecb50d55-ee71-3d44-bac1-2f18aaef1eff | -14.82849 | -47.22792 | 2025-10-05 00:33:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 98f76b7a-139c-32a6-a175-b7add0188778 | -11.54775 | -47.68949 | 2025-10-05 00:33:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e1cb5af7-3a40-3af0-a621-6652c54d9494 | -11.93161 | -46.43888 | 2025-10-05 00:33:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d0c706b1-533f-35c3-a3f1-65fc83409836 | -13.08608 | -47.88727 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 05d925d3-379e-36c8-8add-ac65bcbd3902 | -15.44732 | -44.29422 | 2025-10-05 00:33:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 86ce25db-38de-3041-a0f9-41c4fd64330e | -8.14674 | -44.0945 | 2025-10-05 00:33:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3806b8bc-c4c8-3d17-a429-e5a2b897d21c | -10.49906 | -48.10024 | 2025-10-05 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c5857f7d-bc95-3ed2-82ad-6c7b48dbbb13 | -9.1594 | -49.95232 | 2025-10-05 00:33:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2b2ad7d1-8e79-3f66-a8c4-0a459d7c7c6c | -10.80952 | -48.81648 | 2025-10-05 00:33:00 | TERRA_M-M | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 707a1106-30f5-34ca-a9c5-ba3820055442 | -15.29671 | -47.94999 | 2025-10-05 00:33:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 1a12c740-be80-3899-9376-c32121a06c9f | -13.35097 | -47.59387 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7ac14090-7776-37fa-a2f3-fe05af8f530d | -13.14275 | -47.95511 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| be49dc9a-7e65-3f94-b047-620d81f013ef | -12.32462 | -55.16089 | 2025-10-05 00:33:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 4629f1ea-2110-33d3-a62f-11aa5c6fb2c0 | -14.00309 | -48.6619 | 2025-10-05 00:33:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| e4ddafbe-3bda-3c38-bda6-8b577c1ed9a6 | -9.1275 | -44.40494 | 2025-10-05 00:33:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d8bc3533-bba1-39f7-9d30-66865104d6c6 | -12.45747 | -44.73362 | 2025-10-05 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 1a4a2fb9-f67b-33ad-9145-40c5071ef174 | -8.54024 | -46.3178 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 29a9f45a-3804-3425-bb1b-3da9248c8ff7 | -10.84124 | -57.17142 | 2025-10-05 00:33:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| d319888f-3bb1-38bb-bad5-7a96787d0a44 | -13.36045 | -48.06716 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f082f06f-79d4-3894-a61f-298a3bd15a78 | -13.73961 | -48.07911 | 2025-10-05 00:33:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c7e1ea04-be43-395f-ba83-d867b4e2dcc4 | -15.57322 | -52.46508 | 2025-10-05 00:33:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| ec66bfd4-bfa2-3d3b-b9c4-d0e058fcf79a | -15.36589 | -47.98019 | 2025-10-05 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 05c02b6e-98e4-34c0-a6ab-8fb8d4276d2e | -13.39126 | -47.56028 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 60f15f8c-dabc-372a-aa1e-fa641d2cd94b | -9.41808 | -49.22262 | 2025-10-05 00:33:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 43daa539-ee22-3475-a7e9-6d39aaefd6af | -8.55327 | -46.31001 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 1de744c6-7abb-3fc6-b2b7-cd67ba11f3f2 | -12.97618 | -51.0318 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 70d901a3-68a6-3560-96af-986b97002928 | -11.11755 | -47.19204 | 2025-10-05 00:33:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1e3dc2e8-4a04-3c0d-8957-f732e9e00515 | -11.87854 | -44.96974 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 77cc16ad-580c-35ef-9c82-66e90e79d24a | -14.41954 | -46.35785 | 2025-10-05 00:33:00 | TERRA_M-M | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6625dac5-1931-3f11-ae23-e736ec698ee2 | -14.67872 | -48.34512 | 2025-10-05 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 70289094-0151-33d0-9d46-1f2b7a4f723a | -13.25242 | -48.49187 | 2025-10-05 00:33:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9aae0eed-2ddc-3206-8c76-43ba87fcdca1 | -13.09998 | -47.85767 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f5db949f-c1e8-3f88-804f-e631044ea2d6 | -13.23348 | -48.48541 | 2025-10-05 00:33:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4b046a53-9d58-3c25-adc4-61e3543d4d64 | -11.12388 | -47.17228 | 2025-10-05 00:33:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4a00a385-e95e-395f-aa8c-4744272ce56d | -13.14567 | -50.93385 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 170.4 |
| e8293482-87ee-3d57-83f6-65bd2d65b007 | -10.50031 | -48.10917 | 2025-10-05 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| a03378ff-f895-3b18-bb5f-bd3283911401 | -12.16847 | -51.42444 | 2025-10-05 00:33:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |


[Clique aqui para ver as próximas entradas](README9.md)
