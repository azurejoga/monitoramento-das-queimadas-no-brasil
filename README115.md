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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 111abd62-b698-35f4-b0f1-0c79db0bbf91 | -16.06681 | -50.44775 | 2024-10-06 05:14:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f5dc81d-260e-3d7b-9c49-19c22484fa7e | -18.40652 | -52.12904 | 2024-10-06 05:14:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 27.3 |
| bf87269e-3d62-338f-8b23-f49a83f3cd66 | -18.69107 | -57.26758 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 69c8ada8-599d-3ecb-a202-b25006d69674 | -18.68752 | -57.26702 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| aa035158-0a25-34d8-8c80-3d404521b77f | -18.68456 | -57.26225 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f92e679f-44ac-3766-9a61-9252dda4139e | -18.68397 | -57.26647 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9d615d24-3349-3389-bc61-c028b4b64cd2 | -17.82582 | -53.78241 | 2024-10-06 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6e0fb12d-f1c9-3f55-bf79-89e70afbfa9e | -17.82535 | -53.78629 | 2024-10-06 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dedf6932-6496-374b-973e-868b606b24e8 | -17.82463 | -53.77062 | 2024-10-06 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cacaf8f5-d0a1-399e-b20f-7f8969abd03a | -17.82399 | -53.77567 | 2024-10-06 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2614e25e-57d4-3e03-8cae-95d28f5fcce2 | -17.82339 | -53.78033 | 2024-10-06 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1dc5506d-5a6d-392d-94dc-e93740acde4c | -17.82319 | -53.7678 | 2024-10-06 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3080b899-7c59-3faf-a8b7-e22c33b152fc | -17.8229 | -53.78418 | 2024-10-06 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b91662eb-dcc8-3aa4-abbb-3f7e011d01ba | -17.82262 | -53.77254 | 2024-10-06 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 06c27243-c681-30c3-bac3-b35e332f8e24 | -17.82242 | -53.78793 | 2024-10-06 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 63d9e4d7-6c3e-393a-8612-86e699308f2a | -17.82203 | -53.77751 | 2024-10-06 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2a1badfb-9dc9-3da0-aa25-e3ec77754ff6 | -17.82153 | -53.78172 | 2024-10-06 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c9270d9a-252d-3c83-990b-4fcb12fee31f | -17.82107 | -53.78545 | 2024-10-06 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4aba643e-7340-3d4d-bdc3-4a8e390fbcc9 | -17.8191 | -53.77969 | 2024-10-06 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b66a9d1c-6d80-382c-bb9e-1265d0bd94d1 | -17.81862 | -53.78345 | 2024-10-06 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6db503f1-da67-34c1-adcf-ab7ef861e129 | -17.81724 | -53.78103 | 2024-10-06 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8633f929-802c-33fc-959d-6274741d637c | -17.81679 | -53.78473 | 2024-10-06 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1b66bd4f-02e1-3050-ab49-1dcff2d3a989 | -17.81433 | -53.78276 | 2024-10-06 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0890cc08-a55d-386c-81d1-3c918fc45262 | -17.81386 | -53.78646 | 2024-10-06 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9aa360cc-6941-3a54-94aa-8b09c8957e61 | -18.68042 | -57.26591 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 801a3b31-6be5-3f46-a3d0-ac37c0ef97a1 | -17.81108 | -53.77394 | 2024-10-06 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 60dc06a4-9afb-3588-ad0e-7cfc304d68b6 | -17.81054 | -53.77823 | 2024-10-06 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0e9734c5-0784-3c47-ba96-2a350efcb5ff | -17.81005 | -53.78207 | 2024-10-06 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 85992d76-4563-3174-9edb-2a972142448d | -17.80958 | -53.78577 | 2024-10-06 05:14:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4889823f-6eff-36b6-82f0-15772541b138 | -18.50881 | -52.92987 | 2024-10-06 05:14:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e176d31-b9f0-3742-ac64-ab119250aa32 | -18.82646 | -53.75642 | 2024-10-06 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 534809f8-f790-330c-89dd-45843622e94c | -18.81721 | -53.75953 | 2024-10-06 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 63401ea1-4111-307b-a782-af58ccfb39d6 | -18.81233 | -53.76323 | 2024-10-06 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f2e567c3-c877-38f2-9f63-370ca5aadc1a | -18.80745 | -53.76693 | 2024-10-06 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5605e88-7b31-3699-abe8-7321a8ceb7ea | -18.80694 | -53.77125 | 2024-10-06 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28dd62dd-3fe4-3947-b2c6-cae4e5b0c95c | -14.15433 | -53.87097 | 2024-10-06 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 330f0db0-3d8d-37ad-9bc0-e98d7018922c | -15.39011 | -53.74431 | 2024-10-06 05:14:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20765cd3-ce9d-38da-a73a-a496b3cb1438 | -17.0157 | -55.05901 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 47b23c17-8651-302d-a5c2-a8e727d2f5dc | -17.01569 | -55.06007 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| c09e7970-602c-3049-934c-dbc0fd3f531a | -17.015 | -55.06417 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| ed93b43f-1db6-3f47-925c-7bc8ca3409e1 | -17.01445 | -55.03875 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4ae3f602-d3fb-3f27-a499-d93bd9ed9b6c | -17.01389 | -55.04292 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| a4c0ad50-91b1-3de0-9113-b15c3501da33 | -17.01378 | -55.04395 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 314fc83f-2376-3640-a92a-9bd0d65cdfcf | -17.01319 | -55.0481 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8d16058f-a7f9-3676-90e1-aa43efabb7d7 | -17.01311 | -55.04914 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4da35cde-5134-3ab1-bed5-39dfc3d5b584 | -17.01249 | -55.05326 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6e765d2b-368f-3764-b92f-cd228066f95a | -17.01244 | -55.05431 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| a8252354-57a4-348f-b480-f224bb572f3e | -17.01178 | -55.05843 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 53692887-b7da-37fb-9e81-1e0f8b3518e8 | -17.01177 | -55.05949 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 4a13bc5f-7e32-3038-bf82-60a23bc02ce1 | -17.0111 | -55.06466 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0621b9f0-7790-35e8-aefb-a714f6af15d6 | -17.01108 | -55.06359 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 0918e192-421c-38a2-95ce-27a1d42e7392 | -17.01068 | -55.03716 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| bab26f6a-ec11-39fc-8b30-3655eb6d3bc6 | -17.01052 | -55.03817 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e0e13915-b034-3d45-9c48-2ba70fb4b383 | -17.01043 | -55.06982 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b6bb3a61-d673-3356-87d2-82cdec4478af | -17.01038 | -55.06875 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0c9637a8-588d-3902-bd3a-733f8a47cb4b | -17.00997 | -55.04234 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 550d1311-ed88-3539-8163-b676ab5e149a | -17.00985 | -55.04337 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| fbe9244d-bd13-395c-830d-31b180a411b4 | -17.00927 | -55.04752 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| ce46790f-cf9b-38c5-84bc-b2e790fe571f | -17.00918 | -55.04855 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0d4e003b-2c5f-3bb5-8bc9-6a45dc8edfe3 | -17.00857 | -55.05269 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5d544ee1-35ad-374b-b2f2-baaa2483e35b | -17.00851 | -55.05374 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f99e8107-d381-3301-8ab1-b275b9dfdc9c | -17.00786 | -55.05785 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 8958e4be-0790-31bf-af68-82d6874ff043 | -17.00785 | -55.05891 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fab0ee9f-b314-34c6-a0b8-2df3500d8c27 | -17.00718 | -55.06408 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a2bbcd31-f498-3e1c-b84d-cb90a651bc81 | -17.00716 | -55.06302 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 568b46b6-f72c-3c16-8174-9c3a50463a50 | -17.0066 | -55.0376 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b292d43c-09c1-3beb-911f-e9085349d8e6 | -17.00651 | -55.06925 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9f28c826-d339-3436-bc8d-8757d1cd0c9b | -17.00646 | -55.06818 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| cd03da91-e2ce-3bee-873c-1ea57c31a3ec | -17.00605 | -55.04177 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| def6892f-85fb-357d-b283-358bb99480cd | -17.00593 | -55.04279 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| e8f13214-a3fa-3105-bc82-3e236e100c2f | -17.00326 | -55.0635 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| afd4ab00-20e7-3f31-b411-fe7582500929 | -17.00259 | -55.06867 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 306486b1-6e51-388c-b89e-987cdcc0b86f | -17.00254 | -55.0676 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d31c6174-0262-3d0a-bdfb-ff5c6919d6af | -17.00212 | -55.04119 | 2024-10-06 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0bcb8509-cc62-343d-aa40-eaa91af34a51 | -16.91377 | -54.55871 | 2024-10-06 05:14:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49ab2174-c7a3-3931-9f48-06064a460be9 | -16.91072 | -54.55051 | 2024-10-06 05:14:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 029b4e64-af58-3f86-92f4-7489595e64fe | -16.91023 | -54.55425 | 2024-10-06 05:14:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f17bb850-366d-334a-8efd-884331808d94 | -18.89287 | -54.54524 | 2024-10-06 05:14:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84e67343-8c0e-334a-b44a-b4076e3c66c0 | -18.88878 | -54.54414 | 2024-10-06 05:14:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ee9ec3f4-009c-32a9-830e-5030106fbcd3 | -18.8844 | -54.47845 | 2024-10-06 05:14:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 465a8db1-bb6b-3cdf-8a83-6010e481b971 | -18.88004 | -54.54639 | 2024-10-06 05:14:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6fd8c3d1-3e7c-39fd-80af-7bdb1c054eeb | -18.87955 | -54.55029 | 2024-10-06 05:14:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2c55fcc1-e38c-3404-ae43-fc5bb7ea6cc7 | -18.87822 | -54.52745 | 2024-10-06 05:14:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7119d8e3-5c44-3f47-84bd-775409864ae9 | -18.87774 | -54.53123 | 2024-10-06 05:14:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4a90ecaf-c0f1-3f16-a10d-4ae9e842c7af | -18.87589 | -54.54581 | 2024-10-06 05:14:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d0cd871d-4496-38f3-8b8d-69742bf04a38 | -18.8754 | -54.54968 | 2024-10-06 05:14:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4ee23517-ff11-3454-8af2-2793c823f7de | -18.87217 | -54.54184 | 2024-10-06 05:14:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a980d6ec-ec5a-3f48-b0cb-13e8514b11c4 | -18.87172 | -54.54535 | 2024-10-06 05:14:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dd079b5a-1122-34d8-821d-258292f89174 | -18.86757 | -54.54475 | 2024-10-06 05:14:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 23e7a534-9714-365a-a28a-c37351252c7a | -18.86035 | -54.4671 | 2024-10-06 05:14:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 40e3e8d1-a47b-3f79-a387-12a77bf9f75d | -20.66301 | -54.88598 | 2024-10-06 05:14:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44b3e99d-c17a-33c4-aefb-a6e9d71c2dde | -19.87651 | -55.084 | 2024-10-06 05:14:00 | NOAA-21 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d29982f-20cc-3e35-b953-d7d9e8a96f36 | -18.67686 | -57.26535 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 748b2bad-0de5-3798-98e7-8034673a9445 | -16.58298 | -55.90867 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 1532c24e-a1bb-39ec-90c3-3196dc3db3f0 | -16.58159 | -56.05716 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4468bc89-ed93-3544-b540-6f21b77afb16 | -16.57989 | -55.90352 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| bb2055e9-caa9-3322-8283-1562b871df97 | -16.57927 | -55.90812 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 4794cc0b-5064-3c34-b021-e5ea7144f87d | -17.02151 | -56.6835 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 4ef5ec22-d977-3c7f-98b4-33c9b73dbf7f | -16.57189 | -55.91905 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 573754d3-b280-302c-b8b5-a218b6784ad5 | -16.5706 | -55.91617 | 2024-10-06 05:14:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |


[Clique aqui para ver as próximas entradas](README116.md)
