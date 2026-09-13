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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc172b35-bb14-3c0e-b514-296ffb13b34c | -7.01255 | -44.63708 | 2026-09-13 03:30:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 44295d27-d8d8-3249-9483-c2cd331e6b93 | -8.27986 | -39.97438 | 2026-09-13 03:30:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6ec01510-4f40-3c5d-b057-e8c14a44a9df | -7.01161 | -44.62285 | 2026-09-13 03:30:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 11021110-186c-3df1-b50f-aa40aacca5ac | -10.30864 | -45.28988 | 2026-09-13 03:30:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 69e9e347-200e-3d79-883d-d8116ea049d7 | -7.01976 | -44.63779 | 2026-09-13 03:30:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2565586c-3236-39db-97b5-7e7615868c93 | -10.25655 | -36.29516 | 2026-09-13 03:30:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| e6e4f9c6-e2a0-33f0-9522-803c0cb46e26 | -9.37744 | -37.23118 | 2026-09-13 03:30:00 | NOAA-20 | SANTANA DO IPANEMA | ALAGOAS | Brasil | 2708006 | 27 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6299d211-cda8-37f7-9d07-f7963cd00886 | -7.01537 | -44.62257 | 2026-09-13 03:30:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f2ebea11-4468-311f-9a51-30db1a99616f | -7.46838 | -42.11785 | 2026-09-13 03:30:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c4f0f400-4c32-3a17-8e19-e2eb99b24669 | -7.014 | -44.6296 | 2026-09-13 03:30:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a7db4f24-c267-311a-9a3e-ed536a1881a8 | -7.96485 | -43.99203 | 2026-09-13 03:30:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8f8828a8-2a8b-339d-a0e6-e72b7ba04a43 | -7.02112 | -44.63079 | 2026-09-13 03:30:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6f7121ab-2893-39a3-b0f5-c364bcc1ce2e | -10.26121 | -36.2995 | 2026-09-13 03:30:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 52.2 |
| d3636eee-1ccf-3c32-a8ef-d629af7d2ea9 | -10.25726 | -36.29879 | 2026-09-13 03:30:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 52.2 |
| 24f8d526-fc9e-3f5e-ad28-7380356cfb4b | -7.96224 | -43.9944 | 2026-09-13 03:30:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a83dc1e1-069f-34e7-a178-cafd0affd66c | -8.28619 | -39.96907 | 2026-09-13 03:30:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ce2562f0-9def-379a-b128-83900d672f8d | -10.30509 | -45.28156 | 2026-09-13 03:30:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f895011e-91df-3e1c-b7c9-be131574f8e8 | -6.82799 | -43.51612 | 2026-09-13 03:30:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dec0adcc-5a82-3dd4-8a47-4d55d277e457 | -10.30327 | -45.28072 | 2026-09-13 03:30:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1f6c213a-e2e6-3357-82b8-9240ee3869ed | -5.55375 | -43.43833 | 2026-09-13 03:30:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b690ee2c-677e-31cc-a24e-bfa14ae0395d | -5.55258 | -43.44467 | 2026-09-13 03:30:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8cb3d348-d0c5-3bc5-af31-f49d961c975b | -10.30875 | -45.29959 | 2026-09-13 03:30:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 562b7b83-6ad6-3389-8b0b-63959ee192bd | -15.25562 | -42.79655 | 2026-09-13 03:32:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 98135fa8-c2fd-34fd-acc0-995cdc1be61c | -12.85364 | -44.38575 | 2026-09-13 03:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 24523158-b40f-388d-bed9-81897e771a68 | -16.67129 | -41.85072 | 2026-09-13 03:32:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4cc9f9e3-899a-3138-816d-575d93bd2247 | -11.18771 | -42.79357 | 2026-09-13 03:32:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7eb2c41c-5881-3c14-82c7-5662b2341dd6 | -18.64354 | -41.99394 | 2026-09-13 03:32:00 | NOAA-20 | MATHIAS LOBATO | MINAS GERAIS | Brasil | 3171501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 821fbcc2-aa10-3e2c-b226-ec1edd157921 | -18.6489 | -41.98736 | 2026-09-13 03:32:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 25f91e07-b05c-3beb-a013-628a6f4279fe | -15.23525 | -42.78761 | 2026-09-13 03:32:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1cd321c-7090-3cb6-b221-e2c6f2af12c4 | -15.26108 | -42.79799 | 2026-09-13 03:32:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7ae266bd-d290-35be-b8a6-9f3331fbec5c | -12.85778 | -44.39795 | 2026-09-13 03:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ef0b5e32-8c8b-3b67-94dd-e73366ccb865 | -11.43101 | -45.15185 | 2026-09-13 03:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9763088-0a8d-3276-99ab-a07dbde5da57 | -12.85388 | -44.39269 | 2026-09-13 03:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| c806d4e4-c227-361c-8d95-f59b5853fa18 | -18.64285 | -41.99194 | 2026-09-13 03:32:00 | NOAA-20 | MATHIAS LOBATO | MINAS GERAIS | Brasil | 3171501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 99e900f1-880a-3adb-b567-187ebe1719b1 | -12.85255 | -44.39113 | 2026-09-13 03:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 5e0c1b33-cefb-3235-acb6-bfd09a7f2428 | -18.48042 | -42.81636 | 2026-09-13 03:32:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bf9a0669-2793-3f54-bffd-bd2b798c9c84 | -11.18685 | -42.798 | 2026-09-13 03:32:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d31b82a3-1097-3e72-b5e7-7651e32e2823 | -12.85274 | -44.39808 | 2026-09-13 03:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| ac84251e-44ad-3205-a639-b4205493e12f | -18.48567 | -42.81632 | 2026-09-13 03:32:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8b9087f9-7db1-31db-b06d-4a078a8a9508 | -15.23401 | -42.7897 | 2026-09-13 03:32:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c392b264-50ff-31bd-8a9d-5359706dda02 | -15.91527 | -42.55618 | 2026-09-13 03:32:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 65d21870-6f70-3a51-8e02-a75ca629753a | -14.10087 | -46.364 | 2026-09-13 03:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6f2a1bb5-6a65-33aa-9b71-f3a64a968c0c | -18.48564 | -42.81744 | 2026-09-13 03:32:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7aa7c4ee-e020-3c3a-aa00-e196a20ef9b5 | -13.75435 | -42.60221 | 2026-09-13 03:32:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 39ec7ac0-ca5b-30bc-ae45-31ae81fd7bde | -15.26026 | -42.80197 | 2026-09-13 03:32:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e6eb62f4-8e4c-3a5e-9e2e-3313f39380a4 | -14.10243 | -46.35692 | 2026-09-13 03:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b285223a-5805-3673-886e-25d09b0850ab | -13.752 | -42.59748 | 2026-09-13 03:32:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2640806c-a601-351a-ad82-b651bd79c32d | -14.10633 | -46.36465 | 2026-09-13 03:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0352b901-3b18-3fb3-af17-1a47a15ed5f2 | -13.75514 | -42.59834 | 2026-09-13 03:32:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 9d7b24b4-5995-36e3-8962-0776f38f4e38 | -15.91456 | -42.55967 | 2026-09-13 03:32:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b35fcaee-0d6b-3555-9c3d-37de2dc3a5b5 | -15.29983 | -43.07761 | 2026-09-13 03:32:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ea2b7312-e7da-377e-8307-38c504b329d2 | -18.65086 | -41.98351 | 2026-09-13 03:32:00 | NOAA-20 | MATHIAS LOBATO | MINAS GERAIS | Brasil | 3171501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5eda5928-5b34-3a9d-8970-ecb6d5d96f2a | -11.18178 | -42.79235 | 2026-09-13 03:32:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 20f864a8-f9f1-3511-a828-0ae56dca4589 | -12.85145 | -44.39653 | 2026-09-13 03:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d95c9db8-12d1-3b8c-bfcf-bc59af24ea44 | -11.19539 | -42.78586 | 2026-09-13 03:32:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b9a1c856-afbc-341b-9170-139dfaae86fb | -18.48705 | -42.81079 | 2026-09-13 03:32:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 26b64ab6-d0db-38a4-80bf-43df1aef602a | -18.48703 | -42.80968 | 2026-09-13 03:32:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 70db3f00-96b7-3f75-9acd-eb916ff318d1 | -15.63124 | -43.33226 | 2026-09-13 03:32:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 5513a299-4600-35db-ac48-427ed601b125 | -11.43641 | -45.15994 | 2026-09-13 03:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9efe113-84b6-3479-8e4b-16184c7dcdb3 | -18.64473 | -41.98825 | 2026-09-13 03:32:00 | NOAA-20 | MATHIAS LOBATO | MINAS GERAIS | Brasil | 3171501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 948c81c9-59bb-3cac-9dfa-f1241232ba71 | -18.64965 | -41.9893 | 2026-09-13 03:32:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1818d39d-6332-375e-a4ea-9713c0a5bf40 | -13.75679 | -42.60276 | 2026-09-13 03:32:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a1e45881-cf11-32df-8c8d-1251cd213634 | -13.75124 | -42.60131 | 2026-09-13 03:32:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9031874e-5cc7-317a-86c1-98a7659c5f38 | -12.85501 | -44.38731 | 2026-09-13 03:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 200c97ec-9f7a-3454-9509-06994ce693c7 | -18.48636 | -42.81293 | 2026-09-13 03:32:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 82cb5aa0-abd0-3924-9394-f6ef75109e45 | -14.10797 | -46.35738 | 2026-09-13 03:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| db945eef-af16-3be3-a703-5adfd4a33242 | -15.23446 | -42.79158 | 2026-09-13 03:32:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 508cff03-5a94-3db5-93fd-408009375ff6 | -13.75756 | -42.59885 | 2026-09-13 03:32:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8660287f-9dc4-3613-b21c-24735989551e | -11.1963 | -42.7812 | 2026-09-13 03:32:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 671d3673-11c0-3988-ad07-deb842d7f09f | -13.74882 | -42.60067 | 2026-09-13 03:32:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 897e0497-a7ee-3a6b-998b-c022c07df486 | -18.48045 | -42.81527 | 2026-09-13 03:32:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3a7e8107-c902-3c6b-8b5b-9e61b1d1b6fd | -19.20773 | -46.79256 | 2026-09-13 03:34:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f822dea7-a0a8-31b4-91ff-b4f57fa11473 | -19.86948 | -42.63718 | 2026-09-13 03:34:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f8ea3223-4458-38ca-a27f-d11b0694f99e | -20.04263 | -45.19702 | 2026-09-13 03:34:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e538116a-b446-38be-81d9-c3689e16f244 | -19.2075 | -46.79796 | 2026-09-13 03:34:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a120b65-7f1b-3939-b579-c5397fa9932e | -19.20631 | -46.7985 | 2026-09-13 03:34:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3236e159-4ce2-3e67-ac9f-c11636782c2c | -19.86883 | -42.64027 | 2026-09-13 03:34:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2e8ba96f-4ef6-322c-a7a4-c7a76b6ca505 | -20.04418 | -45.19753 | 2026-09-13 03:34:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c30ee569-4dbd-3590-8e77-e131c64edde2 | -20.04311 | -45.20237 | 2026-09-13 03:34:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| caf14ca7-aba8-3c52-9c12-9d56c6b44131 | -19.20109 | -46.7961 | 2026-09-13 03:34:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c87d8e0f-dc9f-3fec-8315-82893eeedfdd | -10.7015 | -54.1663 | 2026-09-13 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| bb27cf81-d480-3bd3-887e-fdd75ceb16da | -2.6784 | -57.5504 | 2026-09-13 03:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 4987f20b-c042-3c2c-bf7d-416ec0a1c364 | -2.6785 | -57.531 | 2026-09-13 03:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 512b8e6a-c304-3052-8828-f7ec135098c6 | -2.6602 | -57.5313 | 2026-09-13 03:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 0eac6ceb-b74e-3aeb-b930-d8ee332c4fa8 | -10.6827 | -54.1679 | 2026-09-13 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| d8dac7aa-f18c-3719-9872-cf2786c683e2 | -6.1111 | -57.6645 | 2026-09-13 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 610897de-b25c-3d98-9059-768daf70f93d | -2.6785 | -57.531 | 2026-09-13 03:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 60e642a4-401e-382d-ac1d-9e3a39d505e0 | -10.7015 | -54.1663 | 2026-09-13 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 766ad2e9-1bb9-33a4-a374-5438af1336a1 | -2.6784 | -57.5504 | 2026-09-13 03:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 21c24468-c54c-31b5-be80-697a2fa09666 | -10.6827 | -54.1679 | 2026-09-13 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 4d1080bb-06bb-3151-8cd8-788c42e89b55 | -6.1111 | -57.6645 | 2026-09-13 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| eaff705c-19fc-3ad6-9e50-3648500db1b7 | -6.1111 | -57.6645 | 2026-09-13 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 475d638e-6904-35ad-8639-44549f279eaf | -2.6602 | -57.5313 | 2026-09-13 04:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 6c469758-72ad-3067-ac08-61e9b73b0e4e | -2.6784 | -57.5504 | 2026-09-13 04:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 08a2c681-4563-3311-9355-1387e1f865d2 | -2.6601 | -57.5507 | 2026-09-13 04:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| b8307fac-4729-376c-aaca-cbf5b5c0e07c | -10.6827 | -54.1679 | 2026-09-13 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| eabcbcaa-1ed1-3426-bd4e-7b44e7687868 | -10.6824 | -54.1884 | 2026-09-13 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 6181dd68-e1bd-3030-8cd2-533b82dccf6b | -2.6785 | -57.531 | 2026-09-13 04:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 89a73a88-d024-3026-9d2d-5a6c4e0d5164 | -2.6784 | -57.5504 | 2026-09-13 04:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| d9cd8939-250b-3816-91e7-2a9483bd1270 | -2.6785 | -57.531 | 2026-09-13 04:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |


[Clique aqui para ver as próximas entradas](README19.md)
