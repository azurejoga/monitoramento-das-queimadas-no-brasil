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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20b68fda-cb83-3bb5-82b4-febf5e70519c | -23.01095 | -50.42444 | 2025-11-12 00:49:00 | TERRA_M-M | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 0614e0d4-3c29-3b15-a69e-088a369df605 | -21.80933 | -56.30188 | 2025-11-12 00:49:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c9252d92-fe38-304e-883a-f922d2bb7438 | -21.1687 | -48.69786 | 2025-11-12 00:49:00 | TERRA_M-M | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.3 |
| 2b3d37ab-dd74-3457-8ea4-aef7b8fee1d2 | -23.59958 | -49.00854 | 2025-11-12 00:49:00 | TERRA_M-M | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c38724f1-cc57-3131-8fa0-d1b987272133 | -23.00952 | -50.41463 | 2025-11-12 00:49:00 | TERRA_M-M | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 35bb3058-a382-382f-bca7-bce4e0e9793f | -20.88967 | -50.10207 | 2025-11-12 00:49:00 | TERRA_M-M | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 101.0 |
| 1c1cee3a-fe23-3350-b56a-718c982bcf4d | -22.78399 | -51.68797 | 2025-11-12 00:49:00 | TERRA_M-M | LUPIONÓPOLIS | PARANÁ | Brasil | 4113809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 02cc7104-0465-3a13-bad9-20a1b63b15fd | -21.41692 | -48.65151 | 2025-11-12 00:49:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 41.8 |
| ec2bad6e-bf04-3e1e-ad21-671ef5845557 | -21.41908 | -48.65756 | 2025-11-12 00:49:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 37.7 |
| cae71b02-58b5-3947-9794-0d47e6720273 | -23.60127 | -49.01934 | 2025-11-12 00:49:00 | TERRA_M-M | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 419fd0cc-54d7-3d3c-abfa-f71cf624d918 | -16.83394 | -46.08668 | 2025-11-12 00:49:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 611b80c3-26c3-312d-82ad-c22c9e5953ad | -16.44927 | -45.00695 | 2025-11-12 00:49:00 | TERRA_M-M | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 6a4da5fc-0435-3de3-ad11-20aecc26624e | -16.45282 | -44.99986 | 2025-11-12 00:49:00 | TERRA_M-M | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 4d770fdf-4017-3a13-8195-119c209f6763 | -19.84484 | -58.01637 | 2025-11-12 00:49:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.4 |
| ab1ab613-3313-349c-af92-a23c8172946c | -17.83621 | -49.35846 | 2025-11-12 00:49:00 | TERRA_M-M | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 813abf9a-b12c-33ff-a9a6-e0466755805a | -19.75189 | -57.99812 | 2025-11-12 00:49:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 4a8315c7-2546-3fe2-8ea8-fcca4d5c52dc | -19.79765 | -57.97474 | 2025-11-12 00:49:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 52133360-05d7-35cf-8999-10877e0e10ee | -17.12446 | -44.66074 | 2025-11-12 00:49:00 | TERRA_M-M | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 25.6 |
| ccede9f2-6933-30f4-997c-08fe1e27ccb0 | -16.83584 | -46.09325 | 2025-11-12 00:49:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d564c6a9-a7a2-3430-9e6d-b0591de0e0ab | -16.88607 | -51.65797 | 2025-11-12 00:49:00 | TERRA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c5752c0b-2b51-3c92-a12e-037737e1c614 | -19.80524 | -57.98524 | 2025-11-12 00:49:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 564b68a9-6242-3c01-90bf-f3549de9a2cf | -17.12688 | -44.65374 | 2025-11-12 00:49:00 | TERRA_M-M | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | 26.6 |
| d83a0d68-fb33-3482-bd10-52532a3b9622 | -16.88471 | -51.64846 | 2025-11-12 00:49:00 | TERRA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 26.4 |
| c74925b0-5239-32b8-a7bd-2658d92788e6 | -19.75379 | -58.01581 | 2025-11-12 00:49:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.1 |
| d8e73fe0-5ff4-34cb-a7ce-14d476d9f186 | -18.47272 | -53.39861 | 2025-11-12 00:49:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 88b1160a-3106-3b5a-8cf4-d9576d45ce68 | -17.87331 | -48.37962 | 2025-11-12 00:49:00 | TERRA_M-M | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6a8ad459-c88a-3bb6-987f-257fe28886fc | -19.78574 | -57.97617 | 2025-11-12 00:49:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.9 |
| c91c8e56-8bcc-3e43-817a-5b35ec1cf68a | -19.81155 | -57.99095 | 2025-11-12 00:49:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.3 |
| 837461d0-844d-31da-b389-ed23b9eb4e9c | -20.21516 | -56.61187 | 2025-11-12 00:49:00 | TERRA_M-M | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 2d55673c-9075-34a2-97b1-fcbaaf15c96b | -16.54401 | -52.81839 | 2025-11-12 00:49:00 | TERRA_M-M | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0d5eeb82-69fb-320b-ad57-dc56dc4ada78 | -20.20434 | -56.61317 | 2025-11-12 00:49:00 | TERRA_M-M | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 40633f05-c656-3ed3-a9dc-2dfd087bb3f2 | -16.87569 | -51.64982 | 2025-11-12 00:49:00 | TERRA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 92fee3e6-157c-3397-9091-f5e583b7df99 | -18.48164 | -53.39716 | 2025-11-12 00:49:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cec7dcc8-207c-3f4b-ae32-46766300d973 | -17.62804 | -46.71228 | 2025-11-12 00:49:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 02d84954-efe5-3a32-ba13-5a1f58dc01ae | -16.89423 | -51.65081 | 2025-11-12 00:49:00 | TERRA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 63bf030a-dca7-3661-9702-151472b64fb5 | -4.1162 | -47.9919 | 2025-11-12 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| fc58647e-5079-35e6-8770-7c96830344b6 | -2.9982 | -45.1658 | 2025-11-12 00:50:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 3985151e-0ab6-3074-b848-1ff0cb108675 | -4.0976 | -48.0144 | 2025-11-12 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 412.0 |
| 146920ab-1090-3017-8898-ef4b6defcb6d | -20.8886 | -50.0937 | 2025-11-12 00:50:00 | GOES-19 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.0 |
| 85f00d77-160f-3eef-8fcb-b5692e6b663f | -4.1161 | -48.0136 | 2025-11-12 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 233.9 |
| cc839caf-9248-38f0-a043-ab1ee086086e | -4.0974 | -48.0361 | 2025-11-12 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |
| ad3aeb94-ae64-33ea-a5c3-1da6b045736e | -2.9983 | -45.1433 | 2025-11-12 00:50:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 5737c4f2-4f94-3650-a703-1d22b63d3611 | -10.4504 | -44.9516 | 2025-11-12 00:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 57.2 |
| f382130d-9955-3ecf-84dd-0307a1ed0180 | -4.9456 | -43.7194 | 2025-11-12 00:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 09314d79-6b16-3f53-9bed-f98042abe221 | -4.116 | -48.0352 | 2025-11-12 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| a66c57dc-a40a-36fd-8f2b-196118e0df11 | -4.0977 | -47.9927 | 2025-11-12 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| b3b03dcb-fb23-3a57-9e53-ae5f8448972e | -4.9643 | -43.7182 | 2025-11-12 00:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 45d4bc22-6c77-39f5-b223-6a76b33f8005 | -10.45 | -44.9746 | 2025-11-12 00:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 3d4f9089-2180-3324-9467-5c54c2c74164 | -9.44637 | -59.20822 | 2025-11-12 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 4fdd35e8-dcf6-3629-9356-24db3f673f30 | -11.84343 | -57.84998 | 2025-11-12 00:52:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 05d0a233-fa60-3c5c-b7e4-b84d3379f9ef | -13.06074 | -50.2909 | 2025-11-12 00:52:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| cb2d52ba-9f2b-3e12-890d-30c4d2a21e1a | -2.79842 | -52.97247 | 2025-11-12 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 331bfaea-9cdc-3d95-a583-357a38c9db9b | -2.87982 | -51.48484 | 2025-11-12 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 69decd24-53c8-396c-9cda-1be631130f9b | -2.79237 | -51.36097 | 2025-11-12 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0a51ab89-84e4-3787-9e47-339608665c8e | -3.98 | -47.29432 | 2025-11-12 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 2fc53a3d-8804-3d26-82d2-77f57e305b85 | -3.09253 | -49.45441 | 2025-11-12 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| d6eac0db-1971-3d60-a0f1-b8a4e880b224 | -1.78628 | -54.00198 | 2025-11-12 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 03e22c0c-22f0-30c9-9cfd-ee97d44e4f79 | -2.79998 | -52.9833 | 2025-11-12 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 95b50774-d4ef-3f50-b697-0d9169a6f1ff | -4.1048 | -48.00442 | 2025-11-12 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 257.5 |
| eefe6f9a-b5c0-37e9-893a-1e3f6bda2c03 | -4.75606 | -48.83601 | 2025-11-12 00:54:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 41153ad4-bd05-347b-8799-d155b741ef44 | -2.79716 | -52.97883 | 2025-11-12 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| f0dab331-8695-314d-b784-91c7685066c2 | -4.09062 | -48.00623 | 2025-11-12 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| ab7441e8-5066-358e-93b9-e62061e28870 | -2.94203 | -52.33266 | 2025-11-12 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5f5ebff5-d87f-316f-9fb3-f8996699569f | -2.39125 | -49.40196 | 2025-11-12 00:54:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| d5a0d60a-7ee2-3c56-b631-4178620bec65 | -3.49406 | -55.41923 | 2025-11-12 00:54:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9f02b690-6d78-3518-96a2-3ffd548abcb6 | -5.25212 | -48.48375 | 2025-11-12 00:54:00 | TERRA_M-M | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 45a37baf-e9c3-3164-88d8-57c14193e8c8 | -2.86689 | -51.47257 | 2025-11-12 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| e1582dcb-4fb6-338e-a18a-da9ab78b4020 | -2.4856 | -50.25327 | 2025-11-12 00:54:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 8fc18b62-1997-353b-aacb-298521e1c721 | -3.63461 | -50.58434 | 2025-11-12 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| adc1374e-d8c9-3eb2-930a-0c1939eb30bb | -4.10853 | -48.02869 | 2025-11-12 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 226.7 |
| 20b9113f-1d5a-3f6b-8f41-1df8e111554a | -3.08829 | -49.51499 | 2025-11-12 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 67adab71-5e15-379a-bca9-d2986f6f7df9 | -2.86892 | -51.48637 | 2025-11-12 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| d4118809-87dd-3ba3-8bc2-4cea1bd8cc48 | -2.93182 | -52.33416 | 2025-11-12 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4fabd56f-cf14-3ccf-95af-083f8a4a882b | -4.10098 | -48.01172 | 2025-11-12 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 409.8 |
| c41de8bb-f04b-38da-aee1-c46b80b43c43 | -3.39358 | -50.26809 | 2025-11-12 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 24bb70a7-7e8a-3829-a978-8c0007f40969 | -3.95186 | -50.31736 | 2025-11-12 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 670e5df2-f2d8-32e2-8551-a80f60940464 | -6.57259 | -51.11652 | 2025-11-12 00:54:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cba7ed39-f6ab-3999-afba-77292565548e | -4.11219 | -48.05254 | 2025-11-12 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| c0a06f9f-776a-3d0e-ae0d-d438854af7f0 | -3.48313 | -49.96176 | 2025-11-12 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d62faaad-24f6-3970-a37d-95bced0184ac | -3.89217 | -52.11586 | 2025-11-12 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| cf56baab-c3f4-3dbf-8670-9bb23560e435 | -4.86833 | -49.59023 | 2025-11-12 00:54:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 51209012-8d21-3f67-a463-657152d786b2 | -3.243 | -50.03403 | 2025-11-12 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| f2165c09-721c-3fe9-82f6-cd215c781db9 | -2.48807 | -50.27065 | 2025-11-12 00:54:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 0b41b6be-ea69-3d93-96c8-7d069bd4bad0 | -3.08546 | -49.49561 | 2025-11-12 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 944fb687-5b8d-3d77-958b-b8f74fe0fb66 | -2.86497 | -51.4787 | 2025-11-12 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 41873e7a-c585-3e0f-94f3-6a1ed23a6d0c | -4.11514 | -48.00982 | 2025-11-12 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 2c5721e5-f605-34a4-b673-2526f5af40b1 | -2.8778 | -51.47103 | 2025-11-12 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 0a631f4b-3dc5-3d54-8bfb-d287306cba6d | -2.989 | -52.51899 | 2025-11-12 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6d518dca-d462-3c86-877c-2c4f99ae7e95 | -1.10722 | -52.59436 | 2025-11-12 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 995179e4-bb13-3466-8b5d-2c825edd7ea2 | -2.86304 | -51.46484 | 2025-11-12 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| da4051ff-c2a1-3428-85ed-aff2e255c46f | -2.40213 | -49.3947 | 2025-11-12 00:54:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| f3e9a31e-6ddc-3b61-84f3-7b09628b6390 | -4.1186 | -48.03362 | 2025-11-12 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 02c997a2-3ec1-3c00-ac72-3bd0f3308942 | -2.4925 | -50.26429 | 2025-11-12 00:54:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 4906423f-54fd-3af8-8d42-2260df7b54aa | -2.79565 | -52.96799 | 2025-11-12 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f32d6505-8330-3278-804f-b232fca0f157 | -3.36346 | -49.51542 | 2025-11-12 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| de0c0501-99b9-3674-ba7c-c6dd3bd54b2c | -3.90239 | -52.11438 | 2025-11-12 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6f214a7e-df59-347a-903b-5efad036a047 | -4.10449 | -48.03571 | 2025-11-12 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 135.3 |
| ad1de965-ba1c-3f39-ac59-43fd9f4f67f2 | -5.25337 | -48.46794 | 2025-11-12 00:54:00 | TERRA_M-M | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 44863c15-202f-3de9-9334-85695248f797 | -4.09444 | -48.03091 | 2025-11-12 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| d8d0270e-0297-38d0-97a0-e617161a7c3d | -4.75856 | -48.84228 | 2025-11-12 00:54:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |


[Clique aqui para ver as próximas entradas](README4.md)
