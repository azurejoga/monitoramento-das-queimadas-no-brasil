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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c6c0efc-e8d8-3010-88eb-178f3306debc | -15.64562 | -45.90335 | 2026-09-03 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 873f57cc-b943-3374-878c-48e2b5e8949d | -14.95639 | -48.10711 | 2026-09-03 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6230e76-f661-37de-8acf-712d423164b8 | -13.65494 | -43.35986 | 2026-09-03 04:04:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 95b6d2a1-9e0b-3ec9-9e2d-546c4739e09d | -14.95563 | -48.11135 | 2026-09-03 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7850372c-3771-3040-9d55-3807e518edcd | -10.90594 | -47.28738 | 2026-09-03 04:04:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2410d7f3-fe51-33d2-8b71-f20930841ba1 | -13.88217 | -42.43203 | 2026-09-03 04:04:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f3654c17-da80-353d-8d01-78ecdb80f4c3 | -12.05305 | -45.02335 | 2026-09-03 04:04:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23ac12ca-e838-37b1-b5f4-03f13c94e613 | -10.184 | -50.27764 | 2026-09-03 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bfe10d95-136f-3ce5-9153-fa3d0279b84a | -12.09451 | -47.0676 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d4af7f15-e0c0-3e83-b478-ca24cdabaf8d | -11.20286 | -45.03335 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a85efc1-4cc6-3629-ae45-9218a890ddae | -10.18462 | -50.27425 | 2026-09-03 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5232296-c843-35d7-a3b4-f72f40d0c697 | -11.10256 | -47.13877 | 2026-09-03 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0a017df5-e100-366f-b80c-127898f2f72a | -16.48225 | -46.60176 | 2026-09-03 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b41b6d41-2fee-32c4-9adb-cbbe47870a3d | -12.40986 | -44.80207 | 2026-09-03 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| cedfbe01-02fa-3a33-9fa7-3d60171bffaa | -15.64488 | -45.90765 | 2026-09-03 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a4bd10b-8008-30bc-bda8-d68b058016ea | -11.31655 | -50.53152 | 2026-09-03 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcc47eac-1308-391f-a968-8e98d4989e0f | -16.07512 | -46.07385 | 2026-09-03 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 425c5d74-643c-31bc-bcc4-5b86f7fe222a | -12.41203 | -44.81128 | 2026-09-03 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d060bc59-377a-36c0-9d3e-ee55a2e4f009 | -11.33631 | -45.12248 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8266f3ae-6f16-34a4-9453-c39356dc129c | -10.18275 | -50.28445 | 2026-09-03 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35e319fb-4f86-34c4-99b4-c3a8bb6d8f55 | -13.09712 | -44.4958 | 2026-09-03 04:04:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9ba8868-0caf-39ce-95ce-ea4bbd1b3b3d | -12.40404 | -44.81438 | 2026-09-03 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ebd9197c-f37b-35dc-84f2-c0966cd784a4 | -10.14857 | -50.26045 | 2026-09-03 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eda161d3-5e6e-3d2e-94f9-6c206dc7d928 | -10.18337 | -50.28104 | 2026-09-03 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b770ef3c-e8b8-31d6-8431-7c08863da74f | -13.71036 | -42.86797 | 2026-09-03 04:04:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 40e5f006-3e37-307f-bc0e-17efb06b1a42 | -17.5263 | -44.61232 | 2026-09-03 04:04:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 121ffbef-eceb-382c-8672-e3988bb8fc86 | -17.57588 | -44.97207 | 2026-09-03 04:04:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8277dfe6-108c-3c0e-803e-1d5bac00ecda | -10.18649 | -50.26407 | 2026-09-03 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3d6250c-4c95-39be-9fcd-d4e491ce9ee2 | -10.571 | -47.71602 | 2026-09-03 04:04:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 236b5739-17a9-3c87-a59a-ec471cd8d8cc | -12.40477 | -44.81005 | 2026-09-03 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| bda66318-b95f-3921-8991-8e89c35caa7c | -11.31984 | -45.12201 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 78413b66-b860-38c0-aac4-93735a883ba0 | -11.31534 | -45.12585 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 192a5a77-2602-3cd1-a2d6-2c149fd0bbcc | -13.51733 | -43.47141 | 2026-09-03 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5eec4e5d-2ddb-3c59-b6d1-91b4e49b67c6 | -14.05077 | -48.40233 | 2026-09-03 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b641596a-acfd-390f-813d-724675e4a4a1 | -10.34052 | -49.95565 | 2026-09-03 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 959e51ca-8da7-3b3d-9177-e8465603ac58 | -12.09443 | -47.06016 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 07b8e0a6-d496-32d0-9028-c09f18d90634 | -13.7886 | -43.64026 | 2026-09-03 04:04:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4902be5b-b376-3131-ac79-6f771bc11b7c | -10.34514 | -49.95981 | 2026-09-03 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee0c51f1-446e-357e-ab53-788ec486966a | -10.34111 | -49.95245 | 2026-09-03 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0736aadb-b026-3e87-93f3-199b1388a762 | -9.63119 | -54.31443 | 2026-09-03 04:04:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd047b6d-3d53-3360-8473-33d02433bb96 | -12.12981 | -44.17877 | 2026-09-03 04:04:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8883eb8f-9ec4-316b-a980-577bd1008ab8 | -14.95524 | -48.08899 | 2026-09-03 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| de0b3558-2fd1-3e30-933e-e479fed36700 | -16.07382 | -46.07246 | 2026-09-03 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 36e1a8db-79aa-3c95-8e1a-138a0c162533 | -12.12781 | -44.19088 | 2026-09-03 04:04:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ff04e49-3641-3e07-b04f-f7ac73347617 | -15.6831 | -45.89948 | 2026-09-03 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7b4b5cf4-1e87-3ef3-8407-d8b13ccde74d | -17.57457 | -44.97163 | 2026-09-03 04:04:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bea5c90-9464-3874-b703-900975201d65 | -11.25117 | -45.16287 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6cc51459-a13e-3e5c-97ae-2dffd9b81a57 | -10.20795 | -50.28598 | 2026-09-03 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9dc4ef7-a568-3991-921a-8cba9156e5da | -12.12494 | -44.18622 | 2026-09-03 04:04:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ec40bfc-2b4f-3f16-ac5c-ece138214326 | -14.95945 | -48.09 | 2026-09-03 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4dba4b9b-cf75-3d12-a3f2-381631fb5eb9 | -10.76092 | -48.97646 | 2026-09-03 04:04:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 05031e5c-5cb2-3cd3-a4c1-c07ce490f67a | -10.14921 | -50.25706 | 2026-09-03 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8a4c272-da18-34c0-8208-825c26b6c22e | -14.21286 | -42.03889 | 2026-09-03 04:04:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b31e8a20-7b9d-3a9d-8686-140a8059448f | -13.58506 | -47.87894 | 2026-09-03 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fdb396bb-3bee-3978-84e5-4ae927ea5c26 | -10.18524 | -50.27085 | 2026-09-03 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74c00721-62bb-3c79-900d-d1a50029ce78 | -15.33416 | -47.04278 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2ca3c8b0-e113-329b-9090-b9538d4fd4b9 | -15.89092 | -47.68124 | 2026-09-03 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4522879-89fa-3e20-840b-0feff3e7b086 | -12.19583 | -47.07799 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc6e346a-4a6d-3144-8572-78ebbe01e29d | -17.48379 | -47.84712 | 2026-09-03 04:04:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ab86687-2aab-3de7-9b7e-eea32254d2ea | -11.29634 | -45.14711 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6d40cf0-f408-3dce-be0f-bb3e462f5a49 | -17.48714 | -47.85152 | 2026-09-03 04:04:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 901b9c13-cacb-30f1-9cf3-7b2b69ebd36e | -14.03104 | -42.54507 | 2026-09-03 04:04:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| aad51a0f-1d35-3c17-ba03-5e7138e7f0e4 | -11.28654 | -45.15943 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 001a9c65-7704-35dd-a32d-599d2ef5a848 | -11.29101 | -45.17874 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ffe6b90-5d5a-334a-a311-9c1c2df17d70 | -11.28902 | -45.12196 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cceb3f3c-b40c-3623-9066-addaed1c9855 | -12.7252 | -43.28542 | 2026-09-03 04:04:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e423656a-99d8-37a2-8f3a-efde92b189ad | -13.79201 | -43.64085 | 2026-09-03 04:04:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3e7b9e22-703a-3051-9c41-bb53b63be45c | -10.32029 | -49.94854 | 2026-09-03 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf318d2a-0b5f-36a5-b9ef-b146eea790dd | -11.31251 | -50.52374 | 2026-09-03 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b63cd020-9a57-3260-bc1f-bf28ef3f1193 | -11.51779 | -46.90371 | 2026-09-03 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b610d783-4eea-3d33-830d-73880381b0b6 | -11.30125 | -50.52509 | 2026-09-03 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d0961455-6b45-349c-86e5-6915d5935e0e | -10.33993 | -49.95885 | 2026-09-03 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57288dab-100d-34de-875a-5f539b9961e8 | -14.95489 | -48.08765 | 2026-09-03 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 59bb5ed6-8cea-3d69-9c59-acd713aedffa | -11.33929 | -50.54691 | 2026-09-03 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2bdb0ee3-85ef-3d30-aaef-dc5d205f2609 | -14.95937 | -48.11068 | 2026-09-03 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a4439f60-471c-3e8a-8261-7875773dce49 | -11.10166 | -47.13797 | 2026-09-03 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 93da26ea-98d4-3d3e-8c16-cd1864c8b55b | -12.19032 | -47.08498 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 73196445-7d88-39f4-bc55-31449e353252 | -15.58838 | -43.80556 | 2026-09-03 04:04:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 69f25d36-2e66-321d-a91d-ad5f4c3bdd49 | -9.63117 | -54.31408 | 2026-09-03 04:04:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2ac02283-1d1e-38d9-b350-53e470e10dee | -12.08891 | -47.06722 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a1e0e8a0-7ff3-3850-be0e-20d443998d53 | -11.31718 | -50.52813 | 2026-09-03 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0cad4b07-7a2a-3aa5-8953-6f24e56c3692 | -10.18587 | -50.26746 | 2026-09-03 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7cc244b8-7521-3c02-95e5-926e478d9b33 | -12.09521 | -47.06371 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 273a4c92-78a1-3e09-a82b-7dc712a95d6d | -18.16062 | -51.79976 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b748c5b7-f9db-3431-a7f3-7ebac5e11019 | -18.16335 | -51.80133 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| abff6fa5-6e0f-3a2d-ac7b-526e5419a536 | -18.5169 | -48.23309 | 2026-09-03 04:06:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca180737-1483-306a-b76b-a5c4d98e7d88 | -18.77712 | -48.90809 | 2026-09-03 04:06:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| db08f995-4373-3a6c-a8f4-5729b5d64feb | -18.14662 | -51.81664 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 275f1bf2-4777-338e-b2ac-af5ee7881210 | -22.72041 | -43.33176 | 2026-09-03 04:06:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d29f0090-d14d-3f71-9173-83396649720f | -18.83796 | -46.44649 | 2026-09-03 04:06:00 | NOAA-21 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4a552e38-d0e0-3a83-a4ce-aa4df1d925b8 | -18.16448 | -51.80693 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4da0f1e8-3f26-3ca8-be44-6b14b07449c1 | -18.76303 | -48.91373 | 2026-09-03 04:06:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fc29d29-1977-3026-8fab-917effb6acc4 | -20.96915 | -47.41542 | 2026-09-03 04:06:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb2d8a2b-89d6-3cbd-96cd-ca2b0d51d106 | -22.72348 | -43.64318 | 2026-09-03 04:06:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5d67268d-3eef-3a8b-9037-76cd1771a0a0 | -18.16207 | -51.80748 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8f6fa1bd-c308-310f-afa0-f1f3dd2f01d6 | -18.78318 | -48.92193 | 2026-09-03 04:06:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 199f1265-ed6a-3c34-8e85-f481ccf5794f | -18.14215 | -51.81248 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f10661a9-b855-344b-8191-92cc9699cac9 | -18.779 | -48.92106 | 2026-09-03 04:06:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d4971f8e-9f5d-3300-a8c6-2ab3da3f5579 | -18.16631 | -51.79782 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4a9bf384-fa91-3b84-8ff0-24de88f3f47d | -18.13581 | -51.81758 | 2026-09-03 04:06:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |


[Clique aqui para ver as próximas entradas](README22.md)
