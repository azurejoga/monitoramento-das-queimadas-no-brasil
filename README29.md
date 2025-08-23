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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afc37582-5a17-3d96-bb72-abdd52efedfe | -11.77969 | -46.40775 | 2025-08-23 04:02:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ab9d23b-11e0-3f20-8746-f9681054baa9 | -13.62903 | -46.87535 | 2025-08-23 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc1d9cd8-21c1-35d0-80e1-4613e61c5637 | -11.50586 | -50.47336 | 2025-08-23 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b868fea-4564-3e68-aa2a-3cb68add29ec | -13.58298 | -43.35188 | 2025-08-23 04:02:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 39757546-3866-3083-be8e-9d1b6e492829 | -13.41863 | -46.26167 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 4d7e2d3c-dc33-3860-b829-4f948b712f14 | -15.06924 | -47.15449 | 2025-08-23 04:02:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab2cc730-4e47-3868-8d3e-9e07ee0a826c | -13.46678 | -47.03492 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 217ff412-8808-3807-9ee3-25ba62f91e44 | -10.48629 | -46.45969 | 2025-08-23 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3302a57-e8b6-3eb4-b5c6-c692f18bb2a1 | -14.91805 | -47.31893 | 2025-08-23 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 82696dbd-dc9a-38c2-8bb3-246b5b5cd45a | -15.19653 | -48.24154 | 2025-08-23 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 740ef2cb-2e31-3b5f-88a4-a14a716f9294 | -13.4096 | -46.24429 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0aa04f7-a558-3279-aae5-7600584c7729 | -13.3742 | -46.21716 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 1478e772-2c30-3b28-b111-6af0f8b82a8b | -12.95595 | -46.30411 | 2025-08-23 04:02:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68677e14-d7ca-31c8-a8c3-1b02f23470e2 | -11.43837 | -47.33559 | 2025-08-23 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebb5d4d9-7074-3d31-b646-296990133e07 | -10.63192 | -50.14802 | 2025-08-23 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39808b36-71f6-332a-b830-6c59fa0d32ed | -8.29886 | -47.26208 | 2025-08-23 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0b577350-bb03-34ec-9f8e-b56df53ca294 | -11.12526 | -44.75613 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54be03b8-d0ac-394d-9027-532dc1a15bdb | -13.50885 | -47.0597 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77349a38-1cde-3d69-924a-eb1d803f95d7 | -10.7079 | -48.21166 | 2025-08-23 04:02:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c37d56e1-bb43-3d13-8fc4-5e6a29683099 | -11.12591 | -44.77462 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3eeb3105-d071-3838-b837-8c85aee15534 | -12.77982 | -48.707 | 2025-08-23 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 06b167ac-92d2-3749-ac50-a00df63a971a | -13.3772 | -46.2229 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc39c460-974a-337a-bee1-36ca75ed8e31 | -11.12961 | -44.77528 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89351018-5887-3b98-ac8a-f2ff60d5fc37 | -12.17836 | -47.20889 | 2025-08-23 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51564337-11a7-3b51-9741-f1d3d0e70d61 | -14.9476 | -48.01183 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d6577bc-7c82-3991-95c2-4aa0380c7b8b | -11.19396 | -55.03628 | 2025-08-23 04:02:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| adabd4a9-f4c8-3c5a-8f3e-8215f0969537 | -11.17845 | -55.04058 | 2025-08-23 04:02:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c634a815-8459-3cd8-804c-89565ded3c17 | -12.994 | -45.23546 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c5384ae6-7040-3bf2-a83b-eeb5e0e83070 | -14.81448 | -47.95358 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| aa3b8d4a-80a3-3383-9809-de2322915f32 | -11.19672 | -55.04609 | 2025-08-23 04:02:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d543957-8285-3b0a-99be-c33349b0e7da | -11.52272 | -40.70329 | 2025-08-23 04:02:00 | NOAA-20 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f654b844-3d0e-349d-a869-8e51c4177282 | -15.19301 | -48.23657 | 2025-08-23 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62c3d160-ac4f-3d60-9f1f-76719141771f | -12.2993 | -49.99987 | 2025-08-23 04:02:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f40d191-9e38-3179-a026-67662c9f7f04 | -14.37991 | -52.05743 | 2025-08-23 04:02:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a671027-b1e4-3500-b3e1-04fb685d8676 | -14.91399 | -47.31815 | 2025-08-23 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0bbec5b7-1225-36ed-8db2-76f341cc0e2b | -8.66522 | -51.27547 | 2025-08-23 04:02:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32b2a3e9-4a56-321d-b50a-890f778b2b81 | -14.47227 | -46.05346 | 2025-08-23 04:02:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5fbd72f2-de5c-3b1a-8d78-b553b3fb1be8 | -11.13634 | -44.7581 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b3f7823c-5fad-3776-977b-4b08cca7b407 | -11.30314 | -44.9211 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f70ca240-93f8-3a9e-a8c6-555a929b5e19 | -15.1993 | -48.2505 | 2025-08-23 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dd6648b-94d2-388e-9543-e2c630441782 | -11.11786 | -44.75489 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 027c0ffc-7ee1-368c-b98e-b38e86c255f6 | -8.85346 | -49.86153 | 2025-08-23 04:02:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9c48b66-5c36-3423-9b28-daca6e826ca6 | -10.70414 | -48.20608 | 2025-08-23 04:02:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a4df1e6-d047-3fc8-a157-e08e20143898 | -11.13483 | -44.76698 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7c3acd3c-65c0-32fa-bcb4-e571c8b6001c | -12.53951 | -45.61552 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d64444de-dcfa-3f26-b79d-542df030ca97 | -12.9903 | -45.23481 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| dd92f816-b919-3004-a99d-c1a927f6df7f | -14.811 | -47.94867 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9ff8625d-51f9-3695-a3a0-0ed7d475ec97 | -10.08238 | -38.43267 | 2025-08-23 04:02:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4012fe07-6ec0-363b-bab5-cafb6a0f117c | -11.18552 | -55.04176 | 2025-08-23 04:02:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0687f431-3e4e-3783-a45b-4b63c26a8744 | -9.44455 | -47.66129 | 2025-08-23 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d3eaba08-2e79-3078-95ff-869d782bef45 | -15.48547 | -47.60991 | 2025-08-23 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e08c34c-5b91-3c7a-8054-d24bcdd3ce9a | -9.3129 | -40.22187 | 2025-08-23 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 711eb406-6720-3e5f-9b7b-a3a0f8433c3b | -15.5276 | -41.6852 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 18125554-e785-3923-9960-42dfdae25bbf | -9.27926 | -40.54545 | 2025-08-23 04:02:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 15781311-da1d-3e60-bee0-b958c31aa810 | -13.37156 | -47.49127 | 2025-08-23 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 82e006e0-2750-3cb1-860c-ec7894d1406a | -13.05222 | -44.06897 | 2025-08-23 04:02:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2682af42-605e-3bb9-a2fc-715f5d2d0b34 | -13.14099 | -46.91362 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| af3cbd35-c69c-3da2-8368-4476d49ca16d | -14.96895 | -48.67981 | 2025-08-23 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1e32377-038a-35db-af46-2a4f9d09105c | -14.47331 | -48.35163 | 2025-08-23 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00984fc5-b2c8-3411-9653-1c796bf810a3 | -14.37914 | -52.06129 | 2025-08-23 04:02:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77193f8c-c857-3d57-a830-d4d02513a47f | -9.0729 | -49.5168 | 2025-08-23 04:02:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91547a44-df63-3dd8-bf28-55a9539e53d8 | -13.04728 | -46.33358 | 2025-08-23 04:02:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0db5c77-d9a3-365d-b651-210acd21580f | -11.28965 | -44.93265 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d4c5b24-b912-328f-9044-97db71479a30 | -13.4126 | -46.2501 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9852ab5-6f2f-3b93-ae8f-a01b911cf1ea | -12.99556 | -45.22648 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| dfcb9251-ad01-32c2-a1db-230aa9b7137b | -13.16543 | -46.91819 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 74930a75-2289-3526-99d2-b304b0f7c4b9 | -13.0411 | -46.79447 | 2025-08-23 04:02:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68834625-5b36-36fd-8bec-7bba6d1358cb | -11.13567 | -44.7397 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1a278bd-a3a1-3ce7-bdfb-806cd6a11894 | -11.1982 | -55.03913 | 2025-08-23 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88b89bf4-8094-32ce-9d1d-f373272a31d3 | -13.37589 | -47.49141 | 2025-08-23 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0a40493-560a-3dac-a2c6-1f9e92f25ac8 | -13.36337 | -54.40466 | 2025-08-23 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 35b4735f-2886-3a9a-8b08-87591b2bc1f6 | -14.36323 | -52.05378 | 2025-08-23 04:02:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97bcce8c-82d3-3de3-a405-e13d367215b9 | -8.52364 | -48.8317 | 2025-08-23 04:02:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edc251a7-2258-3a59-ac77-ef106af8ad5e | -8.04494 | -47.31169 | 2025-08-23 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a955eb33-ce96-3b6e-8b07-1f40d5559d8a | -11.0559 | -44.59174 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0c303c1-490a-39b6-91c6-13d303bb4050 | -13.37266 | -47.50922 | 2025-08-23 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 07b7548c-f935-34fe-9c93-82144ed644db | -8.65936 | -51.27435 | 2025-08-23 04:02:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0333d6f3-2ae5-38ea-aeae-745b5d778568 | -13.64296 | -46.8908 | 2025-08-23 04:02:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63348286-1429-3708-8c93-51da39e2853d | -11.4391 | -47.33154 | 2025-08-23 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1c8d3e6-bed2-3d33-b135-c14452f82487 | -9.55186 | -47.93608 | 2025-08-23 04:02:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e03c7521-5fd3-35b0-9179-18b6bc8fba97 | -8.7944 | -47.31682 | 2025-08-23 04:02:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de41c060-5fa3-3120-895f-34269a54dcbf | -15.48447 | -47.60853 | 2025-08-23 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1fb6b42-5449-3b61-9f5a-4a566b3c0a5e | -9.6389 | -44.60973 | 2025-08-23 04:02:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 004aa707-7ebe-3781-b06a-260b055e9200 | -8.77511 | -45.43266 | 2025-08-23 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28ee2723-1d50-3b9f-9e16-cde8f7cc2ac7 | -13.12758 | -46.8946 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d906b2ad-0a16-3fee-b032-7831fb0da667 | -8.89525 | -47.33313 | 2025-08-23 04:02:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06203e8a-a175-3f80-b131-b47c279ccdce | -14.90327 | -47.99038 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6a7d631-12c3-355c-b8f2-da0f57f7301e | -14.82634 | -47.96057 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55e033b2-68df-30aa-8a6f-82e0c5066360 | -14.77371 | -45.38662 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9f3c7f7-7930-3aa3-9fb6-d17419deb996 | -9.82698 | -46.37902 | 2025-08-23 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b6943c06-b382-305f-9770-06576bba0e0b | -12.96024 | -46.27962 | 2025-08-23 04:02:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97d76e3b-c204-3361-94ed-846b541c8070 | -9.05805 | -49.53594 | 2025-08-23 04:02:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f9a839c-d5b2-3aa7-adf3-93f3c59a7cb5 | -12.31562 | -49.99687 | 2025-08-23 04:02:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 043f2fb6-d5d2-373a-9801-75927031f306 | -8.85223 | -49.86833 | 2025-08-23 04:02:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa12b9b5-4556-3da2-8bfc-0fc3ad9ff561 | -15.44881 | -41.69081 | 2025-08-23 04:02:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4d51b3b0-0370-3075-89cd-8888ac5719f6 | -14.76982 | -45.2344 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c37dc0b3-843d-3bd5-9455-1262e64011af | -12.18701 | -47.21172 | 2025-08-23 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b78d051c-c83d-33aa-8f38-448f4e66c8d4 | -15.53367 | -41.68988 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 88bbe4dd-1b8c-3e48-9500-2c0e90a9697e | -12.99925 | -45.22715 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d6613014-0a4e-3582-aab7-b254e28c8986 | -14.37668 | -52.04465 | 2025-08-23 04:02:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README30.md)
