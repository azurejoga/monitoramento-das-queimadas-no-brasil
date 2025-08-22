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
| e8be4895-5594-341a-80aa-98fc82b123e1 | -11.44284 | -47.30915 | 2025-08-22 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 72ff31a1-722d-36f9-957a-163a87b63b59 | -13.03448 | -46.32087 | 2025-08-22 03:32:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4f454670-583d-3dee-978f-aa8f73074262 | -14.88159 | -47.9575 | 2025-08-22 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 4c79e011-f9a5-3566-951e-2957ccc7fb1d | -11.31647 | -44.94395 | 2025-08-22 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d0d82e2-5aeb-3939-89e9-334a93fd87d7 | -11.12608 | -44.72041 | 2025-08-22 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1a7fef4-ac20-334b-ba26-547df4b39e15 | -12.56897 | -41.27847 | 2025-08-22 03:32:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8efdc2ce-223a-3435-9791-ce09ad09fce6 | -14.88339 | -47.94973 | 2025-08-22 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7924980c-cebb-3ec0-aeb6-2eb64ac6c282 | -13.03227 | -45.19717 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 448efe08-5d01-3ab2-bac4-943c85cc19ea | -14.30619 | -47.06688 | 2025-08-22 03:32:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0475aa97-65d6-3fa0-9a07-93d271cd78ab | -12.9544 | -46.28509 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5f11905d-17eb-3661-ba39-2dfee0185e4b | -14.53148 | -39.73926 | 2025-08-22 03:32:00 | NOAA-21 | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dc00878a-450a-37e3-b470-f44edc52fa05 | -14.97166 | -47.13624 | 2025-08-22 03:32:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a9336c56-81ee-3a7c-80fb-56df8f98cd0e | -13.00528 | -45.2329 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1a6b2f76-b0b1-3753-ac9a-142a90f4986c | -11.13483 | -44.7079 | 2025-08-22 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 178e540f-580c-3de1-bccf-25d25bd8301b | -12.71346 | -40.89768 | 2025-08-22 03:32:00 | NOAA-21 | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a31e3688-fc2f-3261-bbcb-c8615f254daf | -13.48676 | -47.04203 | 2025-08-22 03:32:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 993c302b-6c83-33ec-b5eb-77dea3233cba | -13.03705 | -45.17394 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 462b7795-854b-3b86-90c1-214e049f906c | -12.9502 | -46.27291 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 38cd70c1-413b-383b-8221-fbec7b5414d1 | -12.93042 | -46.17501 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a250c8db-106a-3d6b-9599-6e0473d5d01f | -12.92638 | -46.19086 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ca3243f7-5d8d-38f2-a999-c100a74ccba7 | -12.00024 | -44.66645 | 2025-08-22 03:32:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a7d75972-1d43-3b68-b104-42ec0f0216c3 | -13.90369 | -43.88657 | 2025-08-22 03:32:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f6f749c-f1ac-31f3-acfc-7da9b6288565 | -12.95178 | -39.55784 | 2025-08-22 03:32:00 | NOAA-21 | ELÍSIO MEDRADO | BAHIA | Brasil | 2910305 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 441bcd54-094d-3ef6-bb7e-fc81f9a695e0 | -13.38162 | -47.49141 | 2025-08-22 03:32:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 33e75d14-250a-35eb-96c6-5e4d24a8acae | -11.12787 | -44.71128 | 2025-08-22 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4fe60c4f-c376-39c4-99c8-ae4166e56ac2 | -13.02815 | -45.1866 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76c44a66-b643-3a3e-96ff-ec203159a7c2 | -12.92945 | -46.17579 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 29490602-268d-3201-97f6-07a3c5e6602a | -13.64534 | -45.71173 | 2025-08-22 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2183c64f-9978-3f1d-8eff-2e8a062ea524 | -11.81029 | -44.25657 | 2025-08-22 03:32:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 11ca8a08-f021-33e7-9b42-d2314cd47241 | -14.76404 | -45.41005 | 2025-08-22 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d92576b6-fd56-3c01-b872-eec088691ba9 | -12.92943 | -46.17969 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e33c056e-95f8-3733-a2f0-1e57a4088ab3 | -13.65155 | -45.71285 | 2025-08-22 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 22470c68-13dc-3126-aef5-50e2951c135a | -15.89403 | -43.45926 | 2025-08-22 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 4a728ea7-869e-3996-99a4-3cdef4251727 | -13.00228 | -45.22022 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a279ea34-ebca-3cfd-946b-136a59d2f5e8 | -14.88883 | -47.95723 | 2025-08-22 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8e4c8007-b3fa-3488-83a5-efa774305c07 | -13.36284 | -46.26791 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 142bb8ad-3a95-34f4-91d1-d67135a3a10e | -13.6371 | -46.87877 | 2025-08-22 03:32:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4374602b-fef0-38e7-9b12-56db790cf2f2 | -12.95973 | -46.25948 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 76ad35ce-683a-3464-ac41-3e89bc9c5032 | -11.80945 | -44.26081 | 2025-08-22 03:32:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5b1bd468-3739-3619-bae9-90a750b714b6 | -11.3086 | -44.95484 | 2025-08-22 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5dbf60e6-6b73-342c-b0d8-781f6b7713e3 | -14.76688 | -45.3964 | 2025-08-22 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 20b4126d-f41e-3231-9a44-9893f1fe24a2 | -14.87801 | -47.9411 | 2025-08-22 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8f225fc8-ef6c-36bb-adb9-6aef9b65cd3e | -14.97948 | -47.13959 | 2025-08-22 03:32:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d55c773e-1cc2-3242-ba98-dd71cdac8a5d | -13.02071 | -45.18714 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0b1abff-7b83-3d0f-a5a3-5353120b4325 | -13.00622 | -45.22819 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d07e999d-33a6-380b-b315-c3549a13f11f | -11.30953 | -44.95011 | 2025-08-22 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5594990-eb6b-314d-b447-52d82dd8b8fd | -13.00111 | -45.22219 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8a5faab3-3ed2-3e9c-8170-9565352141d2 | -12.00895 | -44.66655 | 2025-08-22 03:32:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f246f9c-6bc7-3f36-ad20-d6e9c46793b9 | -14.30494 | -47.07269 | 2025-08-22 03:32:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79a2019a-7cf2-3dc0-a205-3b3276650352 | -13.03007 | -45.17728 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ac1c191-b0ac-3854-b3e1-e9ef0d397068 | -12.57469 | -41.27407 | 2025-08-22 03:32:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0a2295e2-4b22-3c12-bb4e-d34644e9334f | -15.89469 | -43.45601 | 2025-08-22 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 42.8 |
| c91df2ad-cfc2-32bd-9f01-e12d63e08679 | -12.92732 | -46.18972 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6af6d5d5-e07f-3d6c-807e-12925c2dd29a | -13.50156 | -47.05738 | 2025-08-22 03:32:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ede0b1d7-dccd-3bf8-adb5-1de9e9de1840 | -10.97867 | -45.60669 | 2025-08-22 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 90e7c1ae-c4ef-329f-b2f0-cf2d3e131197 | -12.09918 | -43.34206 | 2025-08-22 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a31c3336-fd59-34fa-8de7-c8e43c700a6a | -13.50398 | -47.05931 | 2025-08-22 03:32:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d97abdcb-c6d4-3989-b208-5e63ad579735 | -11.11911 | -44.72375 | 2025-08-22 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5758a425-b82c-3fd4-a57f-df3c35a79d85 | -13.00033 | -45.22961 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c65524f1-b4d5-3b1d-9bdf-6e8c69d00bf3 | -13.63873 | -46.88254 | 2025-08-22 03:32:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b551ace0-715e-3f2d-ad9d-81b22112b467 | -12.99935 | -45.23432 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d4c59acd-dee1-339f-a02e-5120e856c395 | -14.47696 | -48.36082 | 2025-08-22 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81fa7b98-905c-3270-8f66-77969fae6307 | -13.37291 | -47.49907 | 2025-08-22 03:32:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e6ed4637-b798-341e-898c-e2b4863d7311 | -14.97293 | -47.13818 | 2025-08-22 03:32:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 19d73411-1dce-3132-b208-bfef0332ba1a | -14.76001 | -45.39965 | 2025-08-22 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8dd0d942-c674-30fc-8a90-4ef66967a755 | -13.90356 | -43.88644 | 2025-08-22 03:32:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed4568cf-6186-3ad4-b1e1-6687a55a59b8 | -13.50266 | -47.06545 | 2025-08-22 03:32:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 930705cb-d2cb-3811-b8f5-0d550692d043 | -13.03201 | -45.16787 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a1f82f9-1430-3b14-a632-0d4c79e1f6f0 | -12.92422 | -46.17266 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 29e48e52-5e92-3fe6-b300-41a5fba86314 | -13.0318 | -46.33367 | 2025-08-22 03:32:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5b3a7789-2f08-35d7-b784-1dd863265147 | -13.02212 | -45.18527 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b29d8924-4f72-316a-a340-601f30fcdc53 | -14.8904 | -47.95053 | 2025-08-22 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 54102a16-0ae8-3dac-a04e-9decbaa0eabd | -14.97171 | -47.14389 | 2025-08-22 03:32:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3d2adfdd-34d4-3863-b1dc-d9db14a6a297 | -13.02719 | -45.19123 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 782ec6cb-5f30-3174-b6da-0871f90fdd85 | -14.86912 | -47.94883 | 2025-08-22 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 34df337d-fe06-3fec-9aa6-a6280e873b22 | -13.64637 | -45.7067 | 2025-08-22 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 54f830ad-e119-307f-b1c6-f5b57615abbf | -14.8301 | -47.93038 | 2025-08-22 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8d9cf885-2e2a-3948-8f01-0b40021366c0 | -11.31662 | -44.94646 | 2025-08-22 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b895eb3-4b4d-314d-bdea-4cdf5c26ad08 | -14.75122 | -45.41208 | 2025-08-22 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ab7fc87-2007-3719-b137-4a4304fe82f9 | -13.03131 | -45.20185 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1589993f-c6bc-39a2-b1f6-71724c94c1ae | -12.9721 | -42.53139 | 2025-08-22 03:32:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 05ade508-0946-3b65-b988-230d9b4d40e0 | -13.02624 | -45.19588 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8a2a8491-8300-30e8-abc5-d23c7fb3f6af | -13.35775 | -46.26036 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9179e4c6-7f2c-36fc-a0da-b4a28043ba75 | -14.75906 | -45.40422 | 2025-08-22 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 28603507-6531-3949-b633-f94b8805ebdd | -12.56986 | -41.27659 | 2025-08-22 03:32:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3f7e9178-9d1a-3b96-86a2-0fb08c9ebc62 | -13.49337 | -47.04374 | 2025-08-22 03:32:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f618512f-3de9-3b34-8590-acd1c2a55a1c | -14.88879 | -47.95763 | 2025-08-22 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 094a1868-924d-359c-87cf-347fd5ac1b71 | -14.97694 | -47.14338 | 2025-08-22 03:32:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9cd703ed-fe37-3937-b673-1c877f650ae0 | -11.12875 | -44.70675 | 2025-08-22 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a5bed0ea-a1c2-3358-9a51-d770a6e9b62f | -11.43444 | -47.31433 | 2025-08-22 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 23ea62bf-117c-3b9d-970a-551d5eea071d | -11.99934 | -44.67101 | 2025-08-22 03:32:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4d59507b-996a-34ba-82a8-013bcbf14eed | -11.81613 | -44.25771 | 2025-08-22 03:32:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a0e8318-3a30-307d-99a5-2e6d922f6b0c | -12.09438 | -43.33754 | 2025-08-22 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f7a514f-dc04-3366-b683-50d75ac00be5 | -12.99837 | -45.23904 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| af5f0f3f-a042-3d42-854d-574577aa0351 | -10.97975 | -45.60142 | 2025-08-22 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a167ccca-d368-35fd-947b-42a0d3c605e8 | -12.99124 | -45.23989 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 8861cb05-bb50-3404-803b-eb6d9e1b851d | -12.95336 | -46.25774 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55cc9c2d-38e7-34cd-9a02-3d61c8b6e911 | -14.46984 | -48.35956 | 2025-08-22 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c5e797fc-aba2-3010-8069-b3f56526885e | -13.90917 | -43.88773 | 2025-08-22 03:32:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bb585bc-a3f5-3c71-b939-105a19195bf1 | -13.00639 | -45.23087 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |


[Clique aqui para ver as próximas entradas](README9.md)
