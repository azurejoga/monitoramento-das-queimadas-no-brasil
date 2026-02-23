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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a27bc5fb-80c1-30b6-93e4-72be6baf5da6 | 2.77029 | -60.28376 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| befe6d94-4f44-3e67-970c-63583615d705 | 1.20959 | -59.97417 | 2026-02-23 04:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50013df4-128f-3e13-9605-7a07a4f953d1 | 3.1841 | -59.98954 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 309f12cd-8f57-3b47-a37d-e4601cd0c927 | 3.23611 | -59.9282 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3cd17273-560b-3699-b2b1-e4b69f3c542d | 3.34967 | -60.04702 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 078426cc-e70c-3c17-a343-442b719308c4 | -3.14955 | -48.14795 | 2026-02-23 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab3ffab0-b3c5-3599-8297-626a520465f9 | 1.43274 | -59.95797 | 2026-02-23 04:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0a94bd7-7de3-31d1-89fe-458e02d039ce | 3.18257 | -59.99047 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae1458b6-b0d6-390a-bf01-d59ae3a60b4c | 2.77084 | -60.28733 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6c639ca-ad42-3575-b2d4-5e487afe4a8a | 1.43222 | -59.95465 | 2026-02-23 04:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8bdd4b3-8799-32e7-adc5-475be561dd74 | 0.78148 | -51.75613 | 2026-02-23 04:53:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b58086cf-5ad4-3049-a938-d421f1273d8f | 3.18694 | -59.98265 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29ad2e46-2052-3293-93c7-436d7f5489df | 3.22579 | -59.9333 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 401de561-c116-34ae-900f-595550f0b486 | 2.71721 | -60.22976 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fd6ab0f-a2aa-3dd8-b3fc-7277e29d60e5 | -2.03319 | -47.13789 | 2026-02-23 04:53:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af163563-d280-3ecf-9a93-f69cc1876407 | 3.18204 | -59.98698 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6cca618e-d822-3e24-b613-220963276360 | 3.41678 | -59.88783 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d0a31867-6dc1-3451-8bcd-a755cb8950b1 | 3.42322 | -59.89396 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddcc729e-01ee-33ea-a4ca-b2bd245216f8 | 3.42136 | -59.91911 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6adf61c3-a0a8-3b66-864c-2e9a6cff255f | 0.69071 | -51.46007 | 2026-02-23 04:53:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| eb0532cc-57cf-3cae-bd22-5ff021b74c8b | 3.2307 | -59.92902 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ebd3f29-a9ba-3840-9321-205afd2c6f75 | 3.42825 | -61.99188 | 2026-02-23 04:53:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20274324-9d05-3e12-b602-9edbafb076dd | 2.7112 | -60.22702 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9cd6e0aa-909e-384d-83dd-e7a26200251b | 3.20667 | -59.95394 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9374d0c-2a6d-3c12-a27f-6871cc2b2fe3 | 3.1836 | -59.98605 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3b535e5-38e1-38d5-8fa5-d996d9e0c7b4 | 2.71173 | -60.2306 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b002d409-289f-393f-98d9-8ab4c65c0d66 | 1.20384 | -59.97186 | 2026-02-23 04:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0fb642c-4cc2-3006-8722-f2155030fdc6 | 3.20226 | -59.96173 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38910838-ef88-36c9-b1e7-76578ae6dc52 | 1.19859 | -59.97281 | 2026-02-23 04:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b48ef67e-694c-3d6d-836b-4a2b55fa03bb | 2.8402 | -60.78458 | 2026-02-23 04:53:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 862e0089-2458-3257-a3bd-5ce45c344a83 | 3.42627 | -59.91479 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10f5b084-1f37-3949-9a48-171f1b083eb3 | 1.42746 | -59.95884 | 2026-02-23 04:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13265ee5-6519-3689-95a5-3529c6bf7095 | 1.86363 | -60.62431 | 2026-02-23 04:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b318564-50b1-39e4-b1fc-16678960c197 | 3.18852 | -59.98168 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9dcc5de-c620-3a20-9df0-be696026e171 | 3.22089 | -59.93758 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ad1e958-45fc-3c3a-ab97-537feef7d4bd | 3.5337 | -60.89416 | 2026-02-23 04:53:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9be9556d-f810-3c7b-8aa8-d659316692a6 | 3.4227 | -59.89048 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d89f64f-ce0a-3b56-bcf9-26988ab821ce | 2.97726 | -60.27251 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c44edb96-e536-33b1-8b6b-ddeaf911ea5a | 3.21158 | -59.94963 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 945a01fb-138e-3c4a-bbee-0654a8f6ec5e | 2.71226 | -60.2342 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eefe8db6-16fb-3aae-aee3-59244c748b0e | 2.95624 | -60.28306 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fcfda74-64ab-3218-b528-6e214fc28f11 | 2.71279 | -60.23777 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2874b94c-3e93-3278-94e5-f81e83de2934 | 3.35019 | -60.05057 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdc0369c-c1ca-304b-839f-3a8d0bdae06c | 3.42525 | -59.90784 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e10384f-3a1e-32c6-b929-1f749c796dd8 | 3.42576 | -59.91131 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e8741b7-0dc7-3abe-aaf0-720bea66c686 | 2.95571 | -60.27953 | 2026-02-23 04:53:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b45ea20-dd1f-34b6-8fed-4703154d7fc3 | -3.49924 | -48.04011 | 2026-02-23 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9dba43f4-9332-335a-bbf5-a22565896a40 | -20.71847 | -46.54993 | 2026-02-23 04:57:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7b21b24d-3f23-38ef-b7eb-de0feb9528a1 | -20.71884 | -46.54641 | 2026-02-23 04:57:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a80d0c66-6695-3275-9a21-205059af6443 | -20.71709 | -46.54583 | 2026-02-23 04:57:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 815bf7b2-21df-388e-8bdc-a97de9d9e26e | 4.07268 | -61.20667 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f40e4433-3d18-31e1-98d1-d8c82f331c92 | 3.41759 | -59.88629 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae4ed922-7e0b-374b-8e0a-25152611d157 | 4.12013 | -61.17661 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c13bd4f-4198-38b7-a5d1-5a037c4259c8 | 4.12379 | -61.08914 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 30b22ebe-4de4-3b84-96de-2e3106977853 | 3.42447 | -61.99216 | 2026-02-23 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4b94730-d6fb-3f7d-8452-77372ea42b32 | 4.12071 | -61.18029 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d4e64c1-e32f-3f68-bf58-b2319e28d537 | 4.18185 | -60.87839 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 203b4bf0-39b0-3158-9c93-d3809f7b4ab5 | 3.42257 | -59.89411 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45421935-45f0-3d5e-9c17-f68c51c49062 | 4.29345 | -60.76106 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05ec4356-cb62-3f06-acb2-21f2132d7f3a | 2.71459 | -60.2317 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c0914b0-c517-3e6a-a963-3e2b184df62b | 4.09364 | -61.20714 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e73389a-0f18-3bdd-bd3e-64afe9ece09f | 4.08619 | -61.18221 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8e770314-634c-3d77-a052-81f9806004da | 2.95485 | -60.28053 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6a46e3e-8d6f-3720-a007-acccc81fea41 | 3.42391 | -61.98862 | 2026-02-23 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c15611bb-4c21-35ef-8b92-f9839ab3c570 | 3.18838 | -59.97622 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b40dd6d-1854-3413-9ecf-b86892911702 | 3.09249 | -61.54553 | 2026-02-23 05:40:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f58f745-154a-3abc-b93d-0f9f672c5264 | 3.34907 | -60.04544 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f9729ac-f954-31db-bfc6-c21b9d69f708 | 2.71393 | -60.22758 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 267b4cad-d8d8-3ca9-b6c6-bd135e662b0b | 2.71034 | -60.22815 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a0b2a5e-7bf6-3622-9c8a-54fd62394408 | 4.29587 | -60.75755 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f3e6f8c-d56d-329c-a0af-b78badab6a67 | 2.83844 | -60.78146 | 2026-02-23 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e278e611-db69-3bec-8921-c55775427fea | 4.23619 | -60.95401 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9201bc8-db32-366b-b462-d7ea79595b25 | 4.09919 | -61.17636 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10448ff4-5334-3ca3-b966-409f23fa2d34 | 3.18145 | -59.9884 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c56b498-30fd-3871-bfd4-17bf8ada36f1 | 4.17195 | -60.86019 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5782337e-3fb3-351d-b89c-fabef869061c | 4.08966 | -61.204 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80db9d5e-1462-3183-8b85-a94cf21a530e | 4.09697 | -61.18436 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c11d8989-ae4a-3903-8c1a-e52f3b09366e | 4.23499 | -60.94653 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1420039-3c3d-3846-aa16-62bbe82e0dac | 4.15698 | -60.94296 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4bcd8fd-8581-3ac9-9c68-98aa3afaf4c6 | 3.23225 | -59.92611 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5adc43bd-1258-3bea-b778-b4d194a9fd84 | 2.70968 | -60.22403 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1690c633-f81b-310a-b71e-92697baf5406 | 4.28341 | -60.7871 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbe3c05b-b922-3e20-bdaa-7b24999afdd5 | 3.53409 | -60.89181 | 2026-02-23 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9abba838-fa3c-37ba-98c5-88cd4d24a5c1 | 3.21323 | -59.94643 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1708b8a3-4954-3832-90c6-be2f2e0b691a | 4.28684 | -60.78649 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d83de31-abd3-39b1-aa05-15fbdae14472 | 4.11897 | -61.16926 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d3dcb95-e91a-34f3-8344-94a74b215325 | 2.97562 | -60.27303 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0a2e1eb-9a43-356b-a4c8-68ad9b164d0c | 4.20788 | -60.10371 | 2026-02-23 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a9d2f85-498b-3a6a-b5b4-2c8b122bb021 | 4.08841 | -61.17431 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41516a00-9229-33b5-97e9-651d1c1f044a | 4.1118 | -59.88753 | 2026-02-23 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d876ca5-f644-33a9-85cd-a26a45c4a2dc | 3.18375 | -59.97944 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d48926ec-baf0-300c-90d9-f01373cd0933 | 4.11839 | -61.16559 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 614e02ed-6c86-3324-89f3-442e443cacc4 | 4.29303 | -60.76186 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 591153d0-92ba-3854-a2de-8d0240da5dd0 | 3.42781 | -61.99164 | 2026-02-23 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c084320-06d3-33f4-b672-81d6cf979550 | 4.1179 | -61.18451 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15b2389c-b282-3d80-8acb-8fc976fa615c | 3.41941 | -59.92046 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1071c00b-742b-3780-8044-03e899191aa0 | 4.08959 | -61.18174 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f99d687d-3a72-3f12-b045-c18965c6ea17 | 4.22935 | -60.95512 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cb305da7-ca19-3ed5-b753-3bd3313d74af | 4.28399 | -60.79078 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2482106b-501d-3cad-930f-f49ccc0f4e99 | 4.15355 | -60.9435 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README3.md)
