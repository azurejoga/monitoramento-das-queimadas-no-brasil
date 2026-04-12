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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c2ea0e2-a994-3afa-93a7-8ff734e37c9a | 1.2853 | -60.3126 | 2026-04-12 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 5b921a82-cacb-3dc3-afaf-97fa3bd17904 | -9.7934 | -37.4809 | 2026-04-12 00:00:00 | GOES-19 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 125.6 |
| f322ff65-6e64-3c8a-a6e2-f4293119f570 | 2.0138 | -61.1015 | 2026-04-12 00:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 2ec5b628-9fbb-3bab-9b73-3956639dbcec | 2.032 | -61.1013 | 2026-04-12 00:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 6a882495-0fab-3627-a8cb-055500cef65d | 1.2853 | -60.3316 | 2026-04-12 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.8 |
| bdf5e93e-18d6-3764-9f93-864ade9f0100 | 1.2853 | -60.3316 | 2026-04-12 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.2 |
| c5513059-6c2f-3621-abb4-8b01a338f004 | 2.0138 | -61.1015 | 2026-04-12 00:10:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 73.3 |
| de8b5037-d583-3e83-a4e1-c6f9f8123d92 | -9.7934 | -37.4809 | 2026-04-12 00:10:00 | GOES-19 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 114.3 |
| bd4ca75e-9436-3bdf-8a1c-74f1b4a96ac1 | -11.7917 | -43.6163 | 2026-04-12 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 3f91a870-480c-300f-9694-24828ad3a8d5 | 1.2853 | -60.3126 | 2026-04-12 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 9fd18ac7-c0d4-3456-9ecf-ff0a6c4e9e15 | 2.032 | -61.1013 | 2026-04-12 00:10:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 6eb45c13-2586-3faf-839e-970430f51a90 | -22.268 | -48.492901 | 2026-04-12 00:17:00 | METOP-B | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 491c421f-4b7d-3614-a17e-5d6cec7d21fa | -11.7929 | -43.611099 | 2026-04-12 00:17:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c63b0161-c179-3704-8f44-25aa8ccdf104 | -22.2696 | -48.500301 | 2026-04-12 00:17:00 | METOP-B | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 63603516-202b-3ff9-9765-1b1d7665851c | -11.7964 | -43.625 | 2026-04-12 00:17:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 19a5bb55-50a6-31c6-87d0-1e026876b15a | -11.7867 | -43.627499 | 2026-04-12 00:17:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 168ad2c4-9683-3b95-8ee4-a0f82e932635 | -19.987101 | -50.3797 | 2026-04-12 00:17:00 | METOP-B | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dbc313be-c87a-3fd6-8dbd-aec9d1c2dad0 | -19.497499 | -49.2318 | 2026-04-12 00:17:00 | METOP-B | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c58651b7-5690-367f-97ad-6d73194eb0a0 | 2.0138 | -61.1015 | 2026-04-12 00:20:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 7e0e191c-4912-3e53-a71e-769e70852499 | 1.2853 | -60.3126 | 2026-04-12 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 5a76708e-331e-3a49-878b-4098acdaf229 | -9.7934 | -37.4809 | 2026-04-12 00:20:00 | GOES-19 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 137.1 |
| 45e22230-10da-31a2-a713-63916f117f9b | 2.032 | -61.1013 | 2026-04-12 00:20:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 7ac472ef-5939-352f-804e-7c734c7bf36f | -11.811 | -43.6133 | 2026-04-12 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 6ef6f95c-f251-32f7-9d82-84018f67e6f7 | 1.2671 | -60.3127 | 2026-04-12 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 5efee92c-4af3-3846-bb72-3ce5a5af010a | 2.6684 | -61.160198 | 2026-04-12 00:21:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 705df429-6790-3c92-9a25-4c136072f8fd | 2.3723 | -60.935501 | 2026-04-12 00:21:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d849ae38-df7f-3b84-b1d1-504dbf7ac8ec | 1.2671 | -60.308998 | 2026-04-12 00:21:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 59a71d29-1e3a-33ab-867c-9c417c61fb55 | 2.0086 | -61.089199 | 2026-04-12 00:21:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e6ce02cb-a4d4-32b7-af5c-5cfd1fb22501 | 1.2703 | -60.295101 | 2026-04-12 00:21:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9c14bdfb-a31f-382d-893c-711377955f7f | 1.2768 | -60.311199 | 2026-04-12 00:21:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 12cb67bd-2e80-37d1-bdda-960a84a100ba | 2.0254 | -61.061001 | 2026-04-12 00:21:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e1564db4-feb9-30cc-890a-1add5f1cad23 | 1.3473 | -60.6717 | 2026-04-12 00:21:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| eecfcd0e-eb33-382b-b1eb-c9e19b25e45c | 1.3409 | -60.6548 | 2026-04-12 00:21:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c09a6bb4-2cc7-30c9-91c2-a3370a615204 | 1.3768 | -60.632301 | 2026-04-12 00:21:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 987ec47e-8fe4-391c-9070-8eb343a45c21 | 1.2734 | -60.2813 | 2026-04-12 00:21:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a9531edc-192e-3cf6-95a8-e597b0bf4c57 | 1.3638 | -60.644699 | 2026-04-12 00:21:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| efe0dc6a-877e-3502-9343-b188bcd72c2f | 1.3443 | -60.640301 | 2026-04-12 00:21:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 52d56717-e323-3296-86b4-2f2100797405 | 2.0183 | -61.0914 | 2026-04-12 00:21:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c3c64bc9-178a-37a4-b262-19c647848906 | 1.3671 | -60.6301 | 2026-04-12 00:21:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6ca146f7-75ea-306e-bff1-c7e336bfa06b | 1.3507 | -60.657001 | 2026-04-12 00:21:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 87ae211d-6ae9-3c37-9592-d546a83160c0 | 1.3735 | -60.6469 | 2026-04-12 00:21:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| dd2353f3-64dc-3ecf-8261-6cfec570977a | 2.0316 | -61.0784 | 2026-04-12 00:21:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6c1c6962-75e3-31f7-b4b6-b5568adfb3ad | 1.3604 | -60.659199 | 2026-04-12 00:21:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c8a8deae-9b30-368e-88b4-8b33527705ea | 2.0121 | -61.074001 | 2026-04-12 00:21:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c0b955cf-87b9-3daf-bcb4-dfd88f02de45 | 2.0218 | -61.076199 | 2026-04-12 00:21:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 281d8b22-24b6-3774-9172-8f80d37de7ec | 1.357 | -60.673901 | 2026-04-12 00:21:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c40756d2-933d-37aa-afe1-dbf79d01feab | 1.28 | -60.297298 | 2026-04-12 00:21:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0e44500d-19d5-3017-9339-583865f95267 | 2.6719 | -61.1451 | 2026-04-12 00:21:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e8ef7c47-1865-3fe6-a3b5-71bdbeda373b | -11.7917 | -43.6163 | 2026-04-12 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| ba46163f-886b-3dc4-8a73-5f93915b5984 | 2.0138 | -61.1015 | 2026-04-12 00:30:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 69.1 |
| e034c77a-8f29-33ae-b772-853d1168ecd1 | 2.032 | -61.1013 | 2026-04-12 00:30:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 77a586d1-b866-3242-b7bb-3329f9113893 | 1.2853 | -60.3316 | 2026-04-12 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.6 |
| ded3a39e-e2d2-3772-bbd9-937459d1dc22 | 1.2853 | -60.3126 | 2026-04-12 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 5f41ccb2-4a3c-3c88-86a2-b224915a8f15 | -9.7934 | -37.4809 | 2026-04-12 00:30:00 | GOES-19 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 107.4 |
| 5747f16b-f0fb-34ee-955d-010509818213 | 1.2853 | -60.3126 | 2026-04-12 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 4cc88cce-dcb5-309e-859c-0d38d470869f | 2.0138 | -61.1015 | 2026-04-12 00:40:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 68.3 |
| ffe1ef02-e501-36ee-bfd7-ad7870a275f8 | -9.7939 | -37.4545 | 2026-04-12 00:40:00 | GOES-19 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 81.6 |
| 8b6ea03d-4b70-3816-a29f-705a9de94e54 | 2.032 | -61.1013 | 2026-04-12 00:40:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 60.0 |
| b951f0c0-3b82-3f37-bb95-113bcfe3b364 | 1.2853 | -60.3316 | 2026-04-12 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 7e928380-e97b-3c69-be4c-fd529c4249f3 | 1.2671 | -60.3127 | 2026-04-12 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.7 |
| b60276f2-1db1-3387-a088-641277d77c3a | -9.7934 | -37.4809 | 2026-04-12 00:40:00 | GOES-19 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 109.6 |
| 6eca6bd2-cbbb-3984-b886-539ea8023745 | 1.2853 | -60.3126 | 2026-04-12 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.6 |
| ffde8451-c689-3f63-add6-97f5f5fb4735 | -9.7939 | -37.4545 | 2026-04-12 00:50:00 | GOES-19 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 81.6 |
| 8445ad17-c1fb-3465-b08d-a7c734747a42 | -9.7934 | -37.4809 | 2026-04-12 00:50:00 | GOES-19 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 107.7 |
| a0c97ab2-d9e5-3d1f-b5dc-b37c1e14b5c4 | 1.2853 | -60.3316 | 2026-04-12 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 8f7aeeb8-e67c-3a46-9705-2baf66853607 | 2.0138 | -61.1015 | 2026-04-12 00:50:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 37e2e173-b7f6-34d4-8524-116f54307d57 | 2.032 | -61.1013 | 2026-04-12 00:50:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 769ec63f-55f1-3586-8251-c87eae929d4f | 1.2671 | -60.3127 | 2026-04-12 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 266bd2f7-181b-3df7-b117-656763a63d17 | 2.0381 | -61.091 | 2026-04-12 00:53:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b2399c30-7c6f-38ed-b981-10942b39b592 | 1.2758 | -60.312401 | 2026-04-12 00:53:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2d692807-aa0b-347f-8c47-8e06ac196b9e | 1.279 | -60.299 | 2026-04-12 00:53:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 09ea867d-3041-3a1a-ba03-b45795827229 | -11.7961 | -43.6222 | 2026-04-12 00:53:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e99f4957-17b3-36e2-bdb0-3483d3dfbe14 | 2.0249 | -61.1035 | 2026-04-12 00:53:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2b9cffee-a782-3f4b-81ae-eaa3dbc5658e | -22.268999 | -48.499599 | 2026-04-12 00:53:00 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b05332c1-4b80-3648-a351-78bf0224fab7 | 1.368 | -60.665699 | 2026-04-12 00:53:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 512ef731-5b53-31ef-a6e1-ee8c32cf519d | 1.2824 | -60.327999 | 2026-04-12 00:53:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c67b3f47-6ddd-397b-b8ed-ca09a303f8a2 | 2.6753 | -61.1749 | 2026-04-12 00:53:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 74676f06-8297-3be5-8933-2a9040a004a0 | 1.3582 | -60.663502 | 2026-04-12 00:53:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b9414fad-f954-30f6-9dd3-e42f209ec594 | 1.3713 | -60.6516 | 2026-04-12 00:53:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7daafe30-cb25-3ce9-abf3-71d234e30320 | 1.3647 | -60.679798 | 2026-04-12 00:53:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7b1f058c-7ffd-33f1-a00c-98198d76ab8b | 1.381 | -60.653801 | 2026-04-12 00:53:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 21a00394-6684-3718-8410-aaad95983f86 | -15.3802 | -52.746601 | 2026-04-12 00:53:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d103da29-218e-3094-9c86-24ec938ed505 | 1.2855 | -60.314602 | 2026-04-12 00:53:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 82391c78-d2ae-3d9e-aa04-6288fe7d87f4 | 2.0318 | -61.074001 | 2026-04-12 00:53:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| cbe522dd-ed00-3950-a02a-c101e6396d4a | 1.2887 | -60.301201 | 2026-04-12 00:53:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2e20ee96-ff86-3e8d-a59e-08f59548ef8c | 1.3777 | -60.6679 | 2026-04-12 00:53:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1c66804f-b0a3-3779-9812-3625821e48c5 | 2.0186 | -61.086498 | 2026-04-12 00:53:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d6c82690-0f5e-36bf-a7ef-b3ed47209bf1 | 2.0284 | -61.088699 | 2026-04-12 00:53:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d791e0d5-b595-3f0d-a4c0-e82fe92ada69 | 2.0221 | -61.0718 | 2026-04-12 00:53:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c10e09bc-2607-34b2-a915-2acb1e5964c0 | 2.6788 | -61.160301 | 2026-04-12 00:53:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d4eb638d-0ca4-3266-ab23-73f10857631b | 1.3485 | -60.661301 | 2026-04-12 00:53:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 500b74bd-2588-3864-accc-89fc4d3eeb83 | 1.3549 | -60.677601 | 2026-04-12 00:53:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 02c4bdba-a77b-3292-83f6-36b22b62c292 | 2.0152 | -61.101299 | 2026-04-12 00:53:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0e989cc1-d991-3091-b4d6-60717bfed8ff | -11.8094 | -43.633999 | 2026-04-12 00:53:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f92cbbb7-99cc-3004-9f15-cd6fe536b9a2 | -11.8058 | -43.619701 | 2026-04-12 00:53:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b7000cd0-7f6f-3b63-90d6-385bdff9163c | -22.270599 | -48.507 | 2026-04-12 00:53:00 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e2ba3d21-ae64-34e6-997f-0f817543d78b | -9.7934 | -37.4809 | 2026-04-12 01:00:00 | GOES-19 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 110.8 |
| d6271189-13ab-3dc0-96f0-90537d911426 | 1.2671 | -60.3127 | 2026-04-12 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.6 |
| edb2790e-ee44-3147-82ab-0974ece71470 | 1.2853 | -60.3316 | 2026-04-12 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 7456550f-86f5-3a1f-86f1-838ab535ddb0 | 2.032 | -61.1013 | 2026-04-12 01:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |


[Clique aqui para ver as próximas entradas](README2.md)
