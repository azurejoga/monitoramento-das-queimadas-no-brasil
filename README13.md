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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83d25317-832f-3f00-b1c8-0481e412d3e1 | -9.45109 | -64.0437 | 2026-07-17 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ad487ed3-628d-30d8-b064-fb20f303fa62 | -9.45288 | -64.03449 | 2026-07-17 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 98a68666-f057-3c6c-a1ac-6e0d45c3a18d | -10.85751 | -46.51412 | 2026-07-17 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e77ece20-387a-3ad2-a31d-9438093ea3d8 | -13.12946 | -53.78258 | 2026-07-17 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0aba488-ec80-37b5-a2a8-634f6d15290c | -12.6609 | -48.21967 | 2026-07-17 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b91c5639-2225-3ed7-bec9-d70ac81a0d82 | -10.86419 | -46.49991 | 2026-07-17 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f9d8a81-c52e-3293-8b93-7d248242551e | -9.91081 | -53.32212 | 2026-07-17 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bfc0ee3-048c-39d0-9a63-cf80c0a9941e | -10.86219 | -46.51469 | 2026-07-17 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7f3b77a0-0f2f-3d5a-8fd6-955ea6345876 | -9.65131 | -48.57322 | 2026-07-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d4bbf2a-1c34-3b24-9a1b-0c88aa93d1b3 | -13.24788 | -45.11158 | 2026-07-17 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 41.1 |
| b9773b2f-0f65-3316-b5b6-a4e8affb554d | -11.20245 | -49.80271 | 2026-07-17 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f55ecf84-575b-3638-a72f-fb2e9b0fea06 | -12.45295 | -49.58166 | 2026-07-17 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 464d9498-466c-3126-9717-23d16daed787 | -13.50349 | -47.64818 | 2026-07-17 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cac97cb-ef79-38b4-804e-d0f71c845295 | -12.41437 | -58.39849 | 2026-07-17 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d0eee9a-294a-3d3c-9234-bcf69d5e5b4d | -12.45545 | -49.59222 | 2026-07-17 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1e4464e0-bc77-3827-820c-cb98929e8bd7 | -9.64931 | -48.57257 | 2026-07-17 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7801923e-7770-3130-99b8-a414d11c6c78 | -10.82105 | -45.13612 | 2026-07-17 04:57:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dde44aef-0b23-323d-9b32-85a9bb4b7457 | -13.4357 | -43.86101 | 2026-07-17 04:57:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 10777b13-6d04-3f39-b2d7-6011e2ebc82c | -13.55171 | -47.78705 | 2026-07-17 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e3eba451-cb76-3747-b855-de13a9966218 | -9.45106 | -64.04404 | 2026-07-17 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c4d13ec9-e649-36d5-bf98-c2b51dda0322 | -10.03603 | -51.66583 | 2026-07-17 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 608ad25c-e97a-3275-a956-22e515a2ca33 | -10.81795 | -47.39471 | 2026-07-17 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 67fdc23f-6619-356b-9d99-51e730e0da15 | -12.93604 | -56.64612 | 2026-07-17 04:57:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48b6a4cd-e9d3-3518-bacb-794d68106966 | -10.03944 | -51.66636 | 2026-07-17 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 007e2e4e-f9bc-391f-8615-a980a7ef4ad2 | -9.90406 | -53.32106 | 2026-07-17 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dad89aa8-2442-3339-a18a-6d478bd1d2d2 | -12.11316 | -49.94204 | 2026-07-17 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd3106cd-f90c-397e-ba8b-a152ff0c1248 | -14.13993 | -46.26976 | 2026-07-17 04:57:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 369b9db2-d73b-308e-99a7-dc1ef9381df3 | -11.40474 | -47.53045 | 2026-07-17 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cddc1315-1d11-3a5e-bedb-cb1fb57e1da6 | -13.56673 | -47.81077 | 2026-07-17 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21163b1b-1bbe-36fc-aeea-034c9578b266 | -9.91357 | -53.32615 | 2026-07-17 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a1507d1-82ec-3049-89b3-ce266dd0fe39 | -13.5673 | -47.80636 | 2026-07-17 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c3c5d04-77c2-3928-9450-eb284442a63e | -9.90736 | -53.32159 | 2026-07-17 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d4c91a2-8e26-3ebd-bf04-2f9bcdf7e86a | -11.20623 | -49.80327 | 2026-07-17 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcd16262-fba6-380f-8c57-c11ff4cb5efa | -12.44197 | -49.57487 | 2026-07-17 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43433aec-ad5f-3d84-9e50-43ed0c0c6d29 | -13.56223 | -47.81055 | 2026-07-17 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3250cbe6-d687-3106-88fc-c9a934876adf | -17.00509 | -48.28264 | 2026-07-17 04:57:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| adb52898-ef52-3bc0-95e2-a6e6978b6405 | -14.13949 | -46.26872 | 2026-07-17 04:57:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0569f2f-98b4-3d6c-852d-aa40de5f0bd5 | -13.51974 | -47.79909 | 2026-07-17 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc98fb2b-f642-331a-bc8e-9b6f6f0ea2fe | -11.76362 | -49.07806 | 2026-07-17 04:57:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09705fd7-5ce1-3a96-8539-ce407e42c2b1 | -13.50734 | -47.54906 | 2026-07-17 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8331327b-f24b-3abd-9eb4-b670ca4e330c | -13.49393 | -47.65146 | 2026-07-17 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dccbd784-1c02-34d7-92ad-b28ac436817b | -12.11696 | -49.94258 | 2026-07-17 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5d98fb57-9c7f-33aa-85d9-acbab851f036 | -11.18517 | -49.89299 | 2026-07-17 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 897db3e1-c536-3949-9914-9720845f7fbb | -12.19837 | -46.48087 | 2026-07-17 04:57:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da987726-6e94-338b-a1ca-6fa2585f7be4 | -10.85014 | -47.25734 | 2026-07-17 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 842898c5-435c-3ac3-aba8-a8eea164ca0d | -11.20574 | -49.80607 | 2026-07-17 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca965ee6-1d28-3d62-ac7d-6a3b7b5b0e7a | -12.12144 | -49.93841 | 2026-07-17 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b40ab46-98ce-36e2-af0f-2993db06c7f1 | -9.45855 | -64.03606 | 2026-07-17 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d1b2a00e-05d8-3308-b0b3-794bf2f97fac | -12.6598 | -48.22781 | 2026-07-17 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc06e743-7c36-3a5b-b41f-9a53997b73ce | -9.45279 | -64.03479 | 2026-07-17 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8a0f1206-0ecd-30aa-9f8b-3053cb346e28 | -10.82175 | -47.39965 | 2026-07-17 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ecb1e79-476d-3ff2-9d37-9a95211f0ec6 | -13.44191 | -43.85809 | 2026-07-17 04:57:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 73d49773-7ff2-3783-a4f0-142966939941 | -17.00643 | -48.28554 | 2026-07-17 04:57:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e8000a0-5d14-391b-99f6-6b7c0b98dd16 | -12.45288 | -46.50865 | 2026-07-17 04:57:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5899e314-2641-353c-b90a-40fb010f6108 | -13.28497 | -45.20475 | 2026-07-17 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d54c446f-35f5-3edf-9405-a9b8d8ceddad | -9.45929 | -64.03207 | 2026-07-17 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 44b0d4ee-e516-38cb-8174-04e85c774498 | -10.84943 | -46.4679 | 2026-07-17 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dae3e169-a143-3ba5-b613-8e135d20e009 | -13.02665 | -47.93365 | 2026-07-17 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 807b2458-ee6d-3e2a-8627-f50e228df262 | -11.64822 | -48.50407 | 2026-07-17 04:57:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0fda5fbf-d279-3af7-b273-e2466a044e21 | -12.68444 | -48.2066 | 2026-07-17 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ca3af7d8-e0c8-33e1-b5c8-c03427f80198 | -13.54722 | -47.78671 | 2026-07-17 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0a736ed0-18e7-3f51-ab36-dc1c363087d6 | -9.90699 | -53.36799 | 2026-07-17 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0541dad-6783-3f10-8569-237009ae2ae4 | -12.65664 | -48.21902 | 2026-07-17 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de0d6595-91fd-3dd5-a81b-8f799025129f | -13.5634 | -47.80159 | 2026-07-17 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f30e34c4-98f7-30fa-9e2f-9f45ac72bc43 | -12.1975 | -46.48579 | 2026-07-17 04:57:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d3826ad6-6378-39d0-870b-e94040f7cef8 | -9.90753 | -53.3645 | 2026-07-17 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f66db95e-e65a-3cdd-94f3-a48da837bfee | -10.81108 | -46.57743 | 2026-07-17 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d6c2c29-cb89-3ac1-ae29-42f2735796af | -10.84019 | -46.57215 | 2026-07-17 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0901bd83-d142-38ec-a742-61f215005a8d | -12.45615 | -49.58722 | 2026-07-17 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f47c2765-0413-3086-ac60-df7abc069705 | -13.24869 | -45.10483 | 2026-07-17 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 573a86f3-cbab-365e-86ad-cc8e32517691 | -9.84735 | -48.23966 | 2026-07-17 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 763ff913-14bf-389d-b521-78d6e4753ad5 | -9.45691 | -64.04462 | 2026-07-17 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d0ac190a-7c64-3de9-b361-a3ca9b6c628b | -15.23913 | -48.57658 | 2026-07-17 04:57:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f29b9ae-2215-37c2-b3ac-5a6f2ae358dc | -11.9088 | -57.3818 | 2026-07-17 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8554b50b-980c-3e24-a803-54634c4d5675 | -10.78669 | -56.74298 | 2026-07-17 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd366414-e52c-3a76-a9ed-94b9b3f4e45f | -10.86286 | -46.50975 | 2026-07-17 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2a825922-1241-3312-9b0f-76e8ea5bd0e6 | -14.72921 | -47.14488 | 2026-07-17 04:57:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e21a359-b186-37ed-aabc-e69025f5b318 | -10.04286 | -51.66689 | 2026-07-17 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ec9322f-face-30b5-84c6-fcc03b3ad3ac | -10.83623 | -46.56641 | 2026-07-17 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0a8e0168-57af-3c41-a77d-e65344562aed | -9.4578 | -64.04005 | 2026-07-17 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 351ebb31-39c0-3ad1-92e0-e8cf0e2763d4 | -10.04002 | -51.66261 | 2026-07-17 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f6c9517-f413-3fcc-848e-323c90779c38 | -13.28012 | -45.2006 | 2026-07-17 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2521cf7-0ced-3730-aa55-e73fcc9d5871 | -10.82751 | -46.52515 | 2026-07-17 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 89e16313-b191-38b2-9e40-c458be519486 | -10.81625 | -46.53839 | 2026-07-17 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d431ae97-fc0b-32e9-a6f3-6f1d8f5ab787 | -10.82156 | -46.53414 | 2026-07-17 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 504dd5d9-4c3d-3508-ad1c-e6116de468bb | -13.2528 | -45.11559 | 2026-07-17 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 8c363f0a-95e1-39e2-9c38-cee825d29e1a | -10.82221 | -46.52927 | 2026-07-17 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4b127c12-80e1-3aab-b167-f9e1a99aa66a | -11.20196 | -49.80552 | 2026-07-17 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58eb08d8-1377-3cb0-b656-0840be8a36b2 | -14.887 | -48.46769 | 2026-07-17 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1d6b18d-3d36-3bdb-b914-119cddd41cb8 | -12.11384 | -49.93731 | 2026-07-17 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64b44af3-db6c-3629-9ca1-f93430195724 | -13.24829 | -45.10821 | 2026-07-17 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| b8fa105a-394b-337c-b9ef-e04e52a5b040 | -13.28456 | -45.20806 | 2026-07-17 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b1c4c04-0c79-30d0-a498-48c76dcbe80b | -11.63669 | -49.12668 | 2026-07-17 04:57:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be88330e-b8b2-3309-adee-61235a70c68d | -10.82185 | -45.12997 | 2026-07-17 04:57:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ce907a84-b858-3433-9f3d-99efc861dd93 | -10.81633 | -45.13221 | 2026-07-17 04:57:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4464722f-740a-360e-b8f0-40f46f4fcf60 | -9.95535 | -50.55362 | 2026-07-17 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d8f882d-069f-31ad-bf4d-2ef393f01fe5 | -13.2491 | -45.10142 | 2026-07-17 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e1852fea-f049-3c2c-968b-7bf83abe829f | -15.23971 | -48.57225 | 2026-07-17 04:57:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6f33654-2d32-3450-a2a0-ff7e078c4420 | -13.25423 | -54.39304 | 2026-07-17 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 149b1ea4-9517-363a-9e9f-30dd4889506b | -10.86352 | -46.50483 | 2026-07-17 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README14.md)
