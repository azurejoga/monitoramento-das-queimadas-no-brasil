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
| 19991211-8f58-3953-bc6a-b181289e0914 | 1.8317 | -60.8765 | 2025-03-26 03:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 6e09bc2b-1384-3248-9876-d1f4d1ffeb5d | 2.5618 | -60.6975 | 2025-03-26 03:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 30ccb9db-9449-37d9-a579-01a7cd49e37b | 1.8317 | -60.8954 | 2025-03-26 03:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| dd3c0ba1-65cb-3ec7-96e9-40f2aaae50fd | 1.8135 | -60.8767 | 2025-03-26 03:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| fd3bb6f6-327b-3b83-884f-06ba3a87f5fb | 1.8317 | -60.8765 | 2025-03-26 03:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 38f24435-8b58-3733-90f1-b404273f610d | 1.8135 | -60.8767 | 2025-03-26 03:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.4 |
| fb274074-eaf2-3313-8f40-d084947a6a5b | 2.5618 | -60.6975 | 2025-03-26 03:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 81.5 |
| c134836c-bb2e-391c-8913-eb9c86ed515a | 1.8317 | -60.8954 | 2025-03-26 03:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 1c89d1a1-f4ce-3acd-9c75-06dc5cd833d7 | -4.72028 | -37.99253 | 2025-03-26 03:21:00 | NOAA-21 | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 0.1 |
| 9ff2ed35-0918-3b51-a1be-f089c92bfd82 | -6.90252 | -34.94848 | 2025-03-26 03:21:00 | NOAA-21 | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 580bf47b-d3f0-32e2-b43c-a036d82bde00 | -5.97749 | -39.66932 | 2025-03-26 03:21:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d0237ccb-dafe-376e-8a97-d5ba5d78e182 | -5.26104 | -36.69571 | 2025-03-26 03:21:00 | NOAA-21 | PENDÊNCIAS | RIO GRANDE DO NORTE | Brasil | 2409902 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a93e1e74-6ccb-3676-a347-b124dfc386dd | -6.43798 | -37.13432 | 2025-03-26 03:21:00 | NOAA-21 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| af89dcc9-3a25-3b8c-bec5-8a869deecf7d | -5.03953 | -37.6431 | 2025-03-26 03:21:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d7e2a93b-fef3-39c8-9193-1120a94f26ee | -7.06585 | -44.37647 | 2025-03-26 03:23:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9eec4b1-cd9e-3f49-b7e7-902e84643f55 | -11.73166 | -37.61921 | 2025-03-26 03:23:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| aa79caa0-f26f-392c-9074-b6b8d6884f0b | -9.88712 | -38.19074 | 2025-03-26 03:23:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eb73375d-7e2d-3808-adb9-e737cff2300a | -8.45005 | -36.22841 | 2025-03-26 03:23:00 | NOAA-21 | TACAIMBÓ | PERNAMBUCO | Brasil | 2614709 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e79e67db-76be-3263-8059-cf433cb84578 | -10.57977 | -45.13885 | 2025-03-26 03:23:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d47c7c0c-6a7a-3f2d-9028-536333d6512c | -7.94814 | -39.05686 | 2025-03-26 03:23:00 | NOAA-21 | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5636026f-a87b-3eb8-abe7-b82ee09087f3 | -9.88795 | -38.18607 | 2025-03-26 03:23:00 | NOAA-21 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5528c2bc-c3ad-38d0-9726-53e5cbe7a1c4 | -11.0836 | -41.742 | 2025-03-26 03:23:00 | NOAA-21 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| fb7e697b-d7b3-3e47-82d2-3fe4c8c25f44 | -11.6698 | -38.49955 | 2025-03-26 03:23:00 | NOAA-21 | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 16cc41a8-6d33-3e39-bebb-131139068818 | -10.39852 | -37.80653 | 2025-03-26 03:23:00 | NOAA-21 | CARIRA | SERGIPE | Brasil | 2801405 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8e0cf9e8-3505-355b-8e36-b35b8ca7f7b0 | -10.57843 | -45.14536 | 2025-03-26 03:23:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4059e4e0-adad-3e1c-abaf-e90147b6cd1c | -8.39069 | -35.02491 | 2025-03-26 03:23:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 68348bcb-0805-39b3-8fc1-9520090ee577 | -7.04322 | -40.40899 | 2025-03-26 03:23:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 285cbd36-e17b-3fdf-b1f1-f4348e71f79f | -8.13105 | -43.14438 | 2025-03-26 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 48aad177-0cbf-3a4a-8dad-92c7f575ddc6 | -12.11304 | -38.35186 | 2025-03-26 03:23:00 | NOAA-21 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fca192cb-a3c5-3823-9c1a-56c5458a58a8 | -8.87577 | -36.5296 | 2025-03-26 03:23:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8a6752e3-1873-373c-85a3-40848cfd70a3 | -7.04418 | -40.4075 | 2025-03-26 03:23:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b0640a06-3c9c-3214-a282-673c0ee3955a | -11.8234 | -40.41245 | 2025-03-26 03:23:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| b4edb91b-363b-3795-b2b4-36df398fdfac | -7.06131 | -44.38618 | 2025-03-26 03:23:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c0b6143c-e6f3-3777-8f1e-9c69e8b2860e | -8.1246 | -43.14531 | 2025-03-26 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cfa9b390-1baa-3716-9477-6ac8309f43e3 | -6.9629 | -43.01247 | 2025-03-26 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 66072d9e-46ea-361d-b299-d6a3d9a24912 | -6.69903 | -36.68904 | 2025-03-26 03:23:00 | NOAA-21 | PARELHAS | RIO GRANDE DO NORTE | Brasil | 2408904 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| edab9a6a-0639-3f66-bc5c-3a1e6f4d924a | -9.72054 | -37.72123 | 2025-03-26 03:23:00 | NOAA-21 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 51640c27-3156-3da9-9ec7-851272c1f2c6 | -8.61407 | -39.19759 | 2025-03-26 03:23:00 | NOAA-21 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fd039758-97d3-3274-a407-f42c925ee88a | -8.34956 | -36.45362 | 2025-03-26 03:23:00 | NOAA-21 | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d0b33176-bc6b-3027-85c7-f87cc9c6383c | -11.31581 | -39.44258 | 2025-03-26 03:23:00 | NOAA-21 | VALENTE | BAHIA | Brasil | 2933000 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 3cca1a70-97b2-32cd-83c8-61d5692397e0 | -9.56145 | -37.78106 | 2025-03-26 03:23:00 | NOAA-21 | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a734810f-c664-3da2-838e-07476c5f2dc5 | -8.12461 | -43.14313 | 2025-03-26 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b6e689ec-9fb7-325b-a11f-94abe92ec074 | -11.52074 | -41.42053 | 2025-03-26 03:23:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cc3e5448-d96b-3ac5-bead-358adbd6bbe4 | -6.2512 | -40.07549 | 2025-03-26 03:23:00 | NOAA-21 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 0.1 |
| 6ab83831-53fc-3eb4-95a0-d45af7afffbf | -5.98531 | -41.40033 | 2025-03-26 03:23:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 8c4f2971-3a51-39ba-a48d-e071427dca5b | -8.13207 | -43.14127 | 2025-03-26 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 93885599-917d-3caa-883e-17972eaa7fd6 | -10.46721 | -43.67261 | 2025-03-26 03:23:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81e90477-9452-317e-b01a-ff116aeb4ae9 | -8.37689 | -43.96276 | 2025-03-26 03:23:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcb99948-d797-34f8-9fd8-c576e7b01c2f | -7.06257 | -44.37967 | 2025-03-26 03:23:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 565859a1-5dbb-3b93-9a5d-b60959bea579 | -7.05761 | -44.3816 | 2025-03-26 03:23:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 91979edd-c50d-3735-be15-aba2fdedb2ee | -8.50495 | -37.83806 | 2025-03-26 03:23:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 0.1 |
| 8bc21566-727a-3c6b-859b-2a0c6854e8d9 | -13.25251 | -41.33403 | 2025-03-26 03:25:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b016b718-b65f-38af-ab27-8223ce7a9e69 | -16.16234 | -40.32736 | 2025-03-26 03:25:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c2c1b421-c428-34e1-8512-39f165fbeb2d | -12.85947 | -43.73174 | 2025-03-26 03:25:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4e9bf2a-4fc0-3724-8000-d0ece807370c | -17.85971 | -39.86209 | 2025-03-26 03:25:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 614e97a2-2ecc-31d5-a660-9afa9ade5128 | -17.86937 | -39.85948 | 2025-03-26 03:25:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 0119c9c2-2644-31fc-ac54-2ea5a21188f4 | -14.66601 | -39.89012 | 2025-03-26 03:25:00 | NOAA-21 | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2366a04f-4111-3cb0-b762-c49d8cca48b5 | -17.86498 | -39.8585 | 2025-03-26 03:25:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| a25f057c-68d5-3cd2-ac3f-77b8e7e9bf20 | -12.22963 | -41.50352 | 2025-03-26 03:25:00 | NOAA-21 | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 0dc6464f-58fd-3613-ad4a-750829eed870 | -13.25128 | -41.33456 | 2025-03-26 03:25:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e64ffa4e-0d8c-37e4-b3c6-c3957189b564 | -11.77194 | -45.08716 | 2025-03-26 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 989286a3-b761-34e3-b7c6-86c71f404cca | -13.31767 | -41.80088 | 2025-03-26 03:25:00 | NOAA-21 | ABAÍRA | BAHIA | Brasil | 2900108 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c45af693-426a-3c86-aa4f-826a63bdbb3a | -17.7321 | -43.09537 | 2025-03-26 03:25:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 890c5b82-71ed-3b62-8b16-d3f54c79f857 | -17.86143 | -39.85304 | 2025-03-26 03:25:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 2844a1e5-605a-3816-9adc-1a8e4214badc | -18.10998 | -39.95216 | 2025-03-26 03:25:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0222b956-9eb7-37de-8ec5-76e39b83d017 | -12.89931 | -40.46553 | 2025-03-26 03:25:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 0.1 |
| fd2b7de0-64fb-3b9d-8f40-66b786f4a620 | -17.86058 | -39.85755 | 2025-03-26 03:25:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| b2487306-c9a2-3d99-a329-dcbddbee0cd7 | -15.9888 | -41.01018 | 2025-03-26 03:25:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| be01df7d-f104-3d3b-b70d-6f5686b65d80 | -17.86583 | -39.854 | 2025-03-26 03:25:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 256ac442-9617-355c-a6d2-5b4d2de221c8 | -17.59255 | -40.43672 | 2025-03-26 03:25:00 | NOAA-21 | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 13dbcb30-7e75-3ba9-a9d9-4fa420526ce3 | -16.68321 | -43.88373 | 2025-03-26 03:25:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1470d1d3-02a0-348e-9bc3-d35d691a70f0 | -15.54595 | -41.76644 | 2025-03-26 03:25:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 51adf164-a7aa-3745-8ad8-d855dc79ba77 | -16.43977 | -45.73684 | 2025-03-26 03:25:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 81bd2ce1-f768-39db-afb7-565baf665de8 | -12.73021 | -41.88504 | 2025-03-26 03:25:00 | NOAA-21 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| bd66670a-1409-3ba9-be02-5b5ebcab9cad | -17.86412 | -39.86301 | 2025-03-26 03:25:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 1c24cc20-555f-3fcd-aaf4-6cf3736bfbb2 | -16.33227 | -39.4366 | 2025-03-26 03:25:00 | NOAA-21 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.0 |
| a18cbe2f-1ef3-3a01-8ef8-1d6bfb9c4691 | -15.488 | -44.45765 | 2025-03-26 03:25:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8c79ed39-d6d7-3ae4-be8b-453ab7cb0feb | -19.7144 | -40.53981 | 2025-03-26 03:25:00 | NOAA-21 | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 93643fac-c76f-33db-bb71-9b69240b2caa | -20.90887 | -41.71486 | 2025-03-26 03:28:00 | NOAA-21 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0aceb65f-d541-3bb1-9572-293d3a13b428 | -21.15806 | -47.36601 | 2025-03-26 03:28:00 | NOAA-21 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 29f48e0e-a7bb-3c78-8bf2-5f96dd2ffd6e | -21.66302 | -43.59185 | 2025-03-26 03:28:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| b9cc3d9b-a08c-3041-9ea4-095e4d69063a | -20.15394 | -47.32946 | 2025-03-26 03:28:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 010727d7-9bb7-32c0-a9b2-39d64cf2e7e1 | -22.36994 | -46.40138 | 2025-03-26 03:28:00 | NOAA-21 | OURO FINO | MINAS GERAIS | Brasil | 3146008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 52eaacd0-9d33-38bd-8c51-6d2dd2e61239 | -21.4392 | -41.46067 | 2025-03-26 03:28:00 | NOAA-21 | CARDOSO MOREIRA | RIO DE JANEIRO | Brasil | 3301157 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4e4d8af0-bc95-3e5e-98be-a8fce4409fd6 | -19.76928 | -47.93037 | 2025-03-26 03:28:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b8af426e-a125-3559-9167-4abb22968ee8 | -21.78138 | -45.00413 | 2025-03-26 03:28:00 | NOAA-21 | SÃO THOMÉ DAS LETRAS | MINAS GERAIS | Brasil | 3165206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a0ba1b44-01f8-358a-8189-0b2951948adf | -20.47302 | -47.49071 | 2025-03-26 03:28:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6138c630-8ea1-3603-af25-e04412f0af6a | -20.14085 | -47.89144 | 2025-03-26 03:28:00 | NOAA-21 | MIGUELÓPOLIS | SÃO PAULO | Brasil | 3529708 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 362020c5-451b-329d-8c37-6dee3fa57a83 | -21.53135 | -44.42751 | 2025-03-26 03:28:00 | NOAA-21 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9d0ade7e-ea58-3e56-a5bd-d104337a8fc9 | -19.57936 | -43.68462 | 2025-03-26 03:28:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c7e3f7f-b7e3-3016-916c-e617127489e4 | -22.78697 | -43.75841 | 2025-03-26 03:28:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2517dd85-4400-3888-8496-396a86947302 | -19.73332 | -48.51513 | 2025-03-26 03:28:00 | NOAA-21 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1208cf43-c5c9-3bea-8867-22aa523a4c57 | -20.4692 | -47.49172 | 2025-03-26 03:28:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34c74cdd-d779-3d3e-82c3-46a9625600b7 | -20.76325 | -46.77004 | 2025-03-26 03:28:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 501e9731-a65b-3d88-8da9-9e5f967921c4 | -20.76438 | -46.77185 | 2025-03-26 03:28:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bbb44c32-7200-30de-80bd-33e53db9785c | -22.53246 | -46.14652 | 2025-03-26 03:28:00 | NOAA-21 | CAMBUÍ | MINAS GERAIS | Brasil | 3110608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 93955a60-06b4-39c7-84d1-203ca035b6c7 | -20.15243 | -47.33575 | 2025-03-26 03:28:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ff517bda-5d6b-39c8-aa68-176fe7c40295 | -21.86309 | -47.35751 | 2025-03-26 03:28:00 | NOAA-21 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 7142a025-0874-3557-ab0b-42f79e7cc29f | 1.8135 | -60.8767 | 2025-03-26 03:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 35bfc6c4-c010-307a-aa13-6cb6638c5865 | 1.8317 | -60.8765 | 2025-03-26 03:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.7 |


[Clique aqui para ver as próximas entradas](README4.md)
