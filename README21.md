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
| a30f02de-7d64-3326-88bc-75f73c5a5634 | -4.75222 | -45.11632 | 2024-12-03 03:44:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f218aa8f-7815-35b4-8aac-2fcc5e34de26 | -5.81131 | -46.48635 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7977853d-c7a7-3312-a576-8acf9910d434 | -6.68254 | -46.3853 | 2024-12-03 03:44:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d2eaa4ef-dd22-3f82-ab8a-7b1c60c142ce | -5.38561 | -42.95955 | 2024-12-03 03:44:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 75d2f454-0502-3475-9252-b1f2cef70b06 | -4.54993 | -42.9304 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dd9ea748-4b41-34b3-b26e-f1759ca566fb | -8.39674 | -39.70992 | 2024-12-03 03:44:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bf62ea2a-bc22-3086-a885-b14e45ba3455 | -4.74998 | -46.20227 | 2024-12-03 03:44:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ff4e6e0-80f9-3f16-9a4b-ac32181c5a26 | -3.60666 | -45.59517 | 2024-12-03 03:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 198af6c5-0801-3a7e-826a-459540f57950 | -3.33789 | -46.05064 | 2024-12-03 03:44:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 15e773e9-4271-3fe4-b3e9-267f335798d5 | -6.04111 | -44.03678 | 2024-12-03 03:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 072aac0c-c661-3e3d-bee4-264c811b23c6 | -5.81461 | -46.47461 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| a6e264c4-7885-3849-9163-4ecde29e4a75 | -6.94136 | -35.13009 | 2024-12-03 03:44:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0f906a67-6c7c-3353-bd52-20e5d380db85 | -3.85615 | -46.52298 | 2024-12-03 03:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 44e0ef4e-b9b1-3433-abdf-4ff4c27967bc | -4.13392 | -45.82699 | 2024-12-03 03:44:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf09677a-27fa-3452-8411-78579e48e372 | -5.31543 | -39.79558 | 2024-12-03 03:44:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c189df8c-be6b-3d7f-b7df-dc0001f2d7d1 | -9.70201 | -42.89148 | 2024-12-03 03:44:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b470f999-cfe2-3e43-a79e-be70c5198c9c | -4.82515 | -43.43601 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6fa3d87a-b242-3ad2-a10f-08258eecf087 | -10.49579 | -36.71551 | 2024-12-03 03:44:00 | NOAA-21 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e0f8609c-1333-3abc-ad56-7aa42cd2b5b0 | -5.54308 | -43.89532 | 2024-12-03 03:44:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bfa86fd2-0094-3d90-a7c3-7071bba81414 | -3.6029 | -45.59627 | 2024-12-03 03:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7ad5643e-3a18-3380-a92a-ecbb75f7d173 | -5.10941 | -43.21834 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fac99a60-9a00-36b9-92cd-5927556ea35c | -5.16822 | -44.80378 | 2024-12-03 03:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4625bb5-7afe-3a29-b1c9-ef47d2394a0d | -5.79918 | -46.48421 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 790af2fc-4720-3256-8b3d-32e9140ad27f | -5.48233 | -46.3479 | 2024-12-03 03:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe4db75e-8196-37c8-9e2f-9eb06abaf633 | -3.33594 | -46.06134 | 2024-12-03 03:44:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db233655-5dc2-3415-8730-bf70609afc10 | -3.35065 | -44.35621 | 2024-12-03 03:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ccb50d4a-a034-30c1-b654-4b3527166c5d | -3.34955 | -46.05566 | 2024-12-03 03:44:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 3e143794-6abb-316e-b7f5-378957994dc8 | -6.03658 | -42.51763 | 2024-12-03 03:44:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 890a2c2a-259a-38d2-95b6-596170a725a5 | -7.56524 | -45.72831 | 2024-12-03 03:44:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| da0b90ed-45b1-3e1f-b179-82c6c027d2b4 | -5.81286 | -46.48419 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| a3509286-feee-350f-a016-70b16a34835a | -5.14611 | -43.2421 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 91ba0c70-381e-36b5-870b-9b6d3ccfadfb | -4.54686 | -42.9187 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0c2949f3-19be-38a4-b04f-5768c464e9ae | -5.56793 | -44.88675 | 2024-12-03 03:44:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21afee2b-3dda-38a4-b4dd-b3c24a3dc411 | -5.81545 | -46.47001 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| aed2ec67-b461-3281-8841-ad1d961ff337 | -7.80499 | -38.72979 | 2024-12-03 03:44:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dd3a0987-f251-3882-a95b-2437a9be1743 | -10.6559 | -44.49313 | 2024-12-03 03:44:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4a529927-3c21-3c75-b8be-9b96941c0980 | -5.45453 | -43.5792 | 2024-12-03 03:44:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd276e06-2fe8-3f36-86cc-064fc8eee63e | -7.80697 | -38.73322 | 2024-12-03 03:44:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 7.2 |
| bed557a8-43d6-388e-b192-94ea8f5bd1bf | -5.1163 | -43.20787 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 8f308bbd-b231-3036-9b5e-3335097afaa4 | -5.14215 | -43.23543 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0f204073-ac44-3dcb-9524-8f6a7f051d72 | -5.81219 | -46.48134 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 303a1c99-1e44-3a71-859e-a6bf7efca80e | -3.46356 | -42.00362 | 2024-12-03 03:44:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 555bd38d-a714-35c1-821e-cd53f375946c | -4.34677 | -43.74871 | 2024-12-03 03:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9e4b1fb-7a37-3366-bdc7-44629ef92115 | -5.80503 | -46.49276 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2792638b-4e20-351c-b6ff-fa27db31f5d0 | -11.13516 | -37.21247 | 2024-12-03 03:44:00 | NOAA-21 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0d90aca6-6e99-3fa4-a1da-419cbfbc09a4 | -3.35437 | -44.36786 | 2024-12-03 03:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5300943d-8e99-33b8-b351-f171b4f2e311 | -10.65488 | -44.49868 | 2024-12-03 03:44:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 513dd3d9-aa2d-38f4-86fe-3eb2203f6938 | -3.34394 | -46.05222 | 2024-12-03 03:44:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 21.1 |
| a087f705-b958-3f03-931e-0a6da154e09d | -4.81098 | -44.99704 | 2024-12-03 03:44:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c2576c2-c8ef-3fd1-936a-96f930175bb2 | -7.56865 | -45.72844 | 2024-12-03 03:44:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d7ed70d1-8f6a-3815-b488-af11ac99b7e6 | -4.80655 | -45.00043 | 2024-12-03 03:44:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef5e6922-2f85-3b61-b688-09395e660c3e | -6.03109 | -42.52181 | 2024-12-03 03:44:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| ea3ad494-4243-3bcb-94a0-2811a7adbb57 | -10.66081 | -44.49403 | 2024-12-03 03:44:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3590e2c4-f3ec-34ca-a315-66b692cb9684 | -4.47535 | -45.71841 | 2024-12-03 03:44:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79f024a3-6e23-3beb-9ea1-82c0cde02052 | -4.08212 | -47.35057 | 2024-12-03 03:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be6fe7e0-8266-312f-893c-485c1ee3e93e | -5.14805 | -43.23069 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| c852319f-5162-3980-b795-18ceaaf16c75 | -2.88691 | -45.44419 | 2024-12-03 03:44:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3cac11ac-c966-3b0f-a3b9-fbc5048995ed | -4.16656 | -48.59568 | 2024-12-03 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d3545667-ed36-38d7-9dfe-ad105759d4ca | -4.16584 | -48.19137 | 2024-12-03 03:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1934ac85-bd58-3289-af44-55fa241f07d1 | -8.60463 | -41.0135 | 2024-12-03 03:44:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 75466177-3f2f-3b6c-8e22-2616e7142896 | -4.47137 | -45.71704 | 2024-12-03 03:44:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c506856-c788-31b5-8187-17ac694e6fdd | -4.7465 | -45.11574 | 2024-12-03 03:44:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c3a8712f-90ac-3585-96a4-228979ad702c | -5.8077 | -46.47822 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 4245d2eb-33ce-37dd-b6e9-99834a7e4b6b | -5.12224 | -43.20296 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 80df2d15-1c46-3369-b468-235ffeca511d | -6.12499 | -43.96168 | 2024-12-03 03:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ff6dfea4-7301-3c5b-8dff-2e10d59bcd0f | -3.34272 | -46.05866 | 2024-12-03 03:44:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 18193a16-86ca-3f3e-abc4-3ca27dca413b | -5.80254 | -46.50639 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f20c7f42-57f6-35fe-826d-5b6a4ed35857 | -8.52583 | -35.43652 | 2024-12-03 03:44:00 | NOAA-21 | GAMELEIRA | PERNAMBUCO | Brasil | 2605905 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 53560778-5997-3a48-b5f8-ec25609e0bf3 | -4.55178 | -42.91941 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6ef7fa1b-4dbe-392b-8a8d-e4f949d6348e | -5.30312 | -35.47369 | 2024-12-03 03:44:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f84c3e29-65d6-3822-bbb3-e0456be85e5c | -5.81383 | -46.472 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| e9e9782b-fde5-302c-94d8-c3588ac205fe | -7.56303 | -45.72746 | 2024-12-03 03:44:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a32d0bf7-9243-38ef-b220-f4d7b8dd5b4e | -5.81303 | -46.47657 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| c011ef4a-8f86-3d65-b820-4748570000a5 | -6.02542 | -46.24598 | 2024-12-03 03:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c36a04f7-f2ca-311e-a9a0-f518fda330d8 | -3.84995 | -46.52155 | 2024-12-03 03:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5147215c-35b7-3fc2-af8a-711a4b41b9d6 | -5.80084 | -46.47479 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| ef30f4f2-f8a4-329b-92ad-346ff3851f8a | -7.64645 | -36.12543 | 2024-12-03 03:44:00 | NOAA-21 | ALCANTIL | PARAÍBA | Brasil | 2500536 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c448b2b2-5bbc-3007-ac8c-0bf5c2c8c47f | -5.50885 | -44.50174 | 2024-12-03 03:44:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 715e36df-5019-357c-8c67-9a41caf1950d | -6.11831 | -43.96981 | 2024-12-03 03:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a899b135-ca1a-39de-ae7d-0e9f2a01e45f | -3.86672 | -43.35773 | 2024-12-03 03:44:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf7335f1-9365-35f8-ba77-569e57016e58 | -5.80441 | -46.49005 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 328571fd-73cd-367a-aadf-9b010f479c57 | -3.95407 | -46.5013 | 2024-12-03 03:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c1d65038-11d5-39dd-876e-2492896bafce | -6.98339 | -43.51981 | 2024-12-03 03:44:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 3ce43a61-94ab-328c-99ca-4ef2a2754af4 | -5.80196 | -46.50395 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59034445-48dd-3bb9-9d32-6b53f3006780 | -4.7463 | -45.71037 | 2024-12-03 03:44:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 153bf5a2-577e-3afb-9e45-5aeec8ace58a | -4.34731 | -43.74547 | 2024-12-03 03:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a07403e6-8491-3b17-8eed-e14257386568 | -3.34469 | -46.04769 | 2024-12-03 03:44:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 6ef107ca-39b6-3d87-adf1-54599a21590f | -4.55085 | -42.92492 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 68549e7a-af05-3581-8cbc-a5df49b18ac9 | -3.60362 | -45.59195 | 2024-12-03 03:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 229c9bab-e750-32aa-a5d9-48d0b6e7bcd5 | -3.33818 | -46.04835 | 2024-12-03 03:44:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| da1216c0-85c8-363d-a790-e41c2d964e9f | -6.18873 | -43.41222 | 2024-12-03 03:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 192da91b-b033-3628-bba5-c9fb4666e478 | -5.11529 | -43.20618 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5cd8754c-9588-3ece-bdad-7ff37047ac2c | -5.80591 | -46.48796 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e5e6e49d-1074-3d6a-b934-e44624ea054d | -5.11251 | -43.22311 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 85a3b966-fcfa-378e-be63-86357e5dbdbb | -5.1676 | -44.80732 | 2024-12-03 03:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcb2374c-59cf-368d-bf72-75b7e955bcf5 | -3.46612 | -42.00266 | 2024-12-03 03:44:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| bd429101-b935-3693-afa6-f570be5380d9 | -4.44112 | -45.36618 | 2024-12-03 03:44:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d57b9ee3-551c-3ed2-9e53-b8a3caff65d3 | -5.11437 | -43.21912 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 3499f653-69d7-3c37-aa9a-f0b8a9f758f9 | -3.33719 | -46.05487 | 2024-12-03 03:44:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 919047c7-76c0-3f7d-80db-3d5b4d4e06cc | -5.11437 | -43.21179 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |


[Clique aqui para ver as próximas entradas](README22.md)
