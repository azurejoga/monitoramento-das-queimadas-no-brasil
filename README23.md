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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 525b3b6c-156c-3a03-9b60-3e81718743b0 | -18.1977 | -53.3208 | 2025-09-28 03:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 4f0beeb2-2e17-337c-9917-0724d85760fc | -17.7373 | -46.70443 | 2025-09-28 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e565ada-2cdd-3521-8710-03b325a54294 | -19.50333 | -42.13088 | 2025-09-28 03:40:00 | NOAA-21 | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 93e32c76-ee77-3559-a094-bc3484a6d37a | -17.75717 | -48.75212 | 2025-09-28 03:40:00 | NOAA-21 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d949a02e-9fad-3365-bfc2-7fb8863cfded | -19.31197 | -43.81705 | 2025-09-28 03:40:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 852282a4-2e5e-3dac-aafa-112b1c1fea4a | -19.65715 | -45.97216 | 2025-09-28 03:40:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 647cced2-3a58-3c09-9811-0cd59b576033 | -21.39298 | -44.00527 | 2025-09-28 03:40:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9d6427c5-4a40-3efe-88f3-a6762e12433f | -21.07296 | -48.66803 | 2025-09-28 03:40:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| aa6ee805-7926-3a33-99c6-0f0dc2fe021b | -18.91221 | -41.12429 | 2025-09-28 03:40:00 | NOAA-21 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ce95007c-0975-3db0-b33e-0c155312e0a2 | -20.52387 | -43.04378 | 2025-09-28 03:40:00 | NOAA-21 | GUARACIABA | MINAS GERAIS | Brasil | 3128204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3cb3bc7f-3515-32d0-9892-503c0dce3e06 | -21.40032 | -40.9991 | 2025-09-28 03:40:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| eee6e021-ea22-3cd5-a3da-d286236fb3e2 | -19.1107 | -41.61012 | 2025-09-28 03:40:00 | NOAA-21 | TUMIRITINGA | MINAS GERAIS | Brasil | 3169505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c5025469-7fee-3cf3-9eaf-c7295fae5cee | -19.10965 | -41.61193 | 2025-09-28 03:40:00 | NOAA-21 | TUMIRITINGA | MINAS GERAIS | Brasil | 3169505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6130210a-2ba1-3355-b67e-00d30ed10882 | -17.72385 | -46.71311 | 2025-09-28 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7333adae-6102-392b-8a8a-36d200397b3f | -19.24627 | -44.07912 | 2025-09-28 03:40:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 736af93a-ba90-30c6-9917-5779b12607b3 | -23.15321 | -47.06134 | 2025-09-28 03:40:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b83cc5a5-5fb1-39e9-a0aa-282721090654 | -17.7581 | -48.76179 | 2025-09-28 03:40:00 | NOAA-21 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b17ad51e-33db-3b4e-a713-99e6935c3b94 | -19.96286 | -41.72829 | 2025-09-28 03:40:00 | NOAA-21 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a00f5a99-a63b-3fcb-9d11-b7786331f9db | -20.69659 | -50.70996 | 2025-09-28 03:40:00 | NOAA-21 | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9fb2e45e-a424-371f-8bae-174871b682be | -17.18289 | -43.39195 | 2025-09-28 03:40:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 85c6c0d4-a105-3603-b80e-e523ced85440 | -23.15251 | -47.06459 | 2025-09-28 03:40:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9266f86b-79f6-3b73-893e-77b5da55f6dd | -19.20857 | -43.97996 | 2025-09-28 03:40:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f34984bb-15c0-34f6-93ea-798b96f48571 | -21.11964 | -42.90102 | 2025-09-28 03:40:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 43388fda-2655-3c93-8282-202345566301 | -18.9074 | -41.12887 | 2025-09-28 03:40:00 | NOAA-21 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| b89994b5-050a-349a-9f83-f53784169f35 | -19.65651 | -45.97523 | 2025-09-28 03:40:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa309495-471d-30a6-b2f9-c132d96ab818 | -17.18381 | -43.38719 | 2025-09-28 03:40:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1d2906ea-2383-37bf-ba4d-eac960257d26 | -19.85781 | -42.59229 | 2025-09-28 03:40:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8aba4eb5-6dcf-32e8-aa49-1373a11555a0 | -19.24529 | -44.08407 | 2025-09-28 03:40:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f87386e3-d2ed-3b03-aad6-de10bafb4e8f | -17.73185 | -46.70276 | 2025-09-28 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71846855-6cb5-30ca-a64d-0e2ca6c848fb | -19.86532 | -43.8042 | 2025-09-28 03:40:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 7d7362eb-1c88-3292-ab85-cc1c651fcd34 | -17.18653 | -43.37318 | 2025-09-28 03:40:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea04b861-889e-33ba-a3f0-5239307d99ea | -19.24169 | -44.0782 | 2025-09-28 03:40:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7cc0fdc-7c84-3631-a481-14fea671edd7 | -17.73261 | -46.69915 | 2025-09-28 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76899c1a-d489-3d90-a438-847aa16592c7 | -22.05695 | -43.01598 | 2025-09-28 03:40:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| bddcc542-36b1-33e8-aa0e-0504d0e87721 | -20.6951 | -50.71606 | 2025-09-28 03:40:00 | NOAA-21 | GUZOLÂNDIA | SÃO PAULO | Brasil | 3518909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 906939d2-dd4c-3191-875a-cbe8abf574cd | -17.71997 | -46.70405 | 2025-09-28 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1676c2c8-1410-3065-b104-7574e93d8ba6 | -22.89514 | -43.58614 | 2025-09-28 03:40:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7a7ffeb2-3d70-3920-922a-0c9d5357fed7 | -17.72469 | -46.70916 | 2025-09-28 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8391a72a-b837-3775-9df1-e19c86ac6882 | -19.03987 | -40.95801 | 2025-09-28 03:40:00 | NOAA-21 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 67ef09b2-7f5f-3e07-a527-d9eb54e30799 | -17.24876 | -43.87271 | 2025-09-28 03:40:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e40f960-6ec4-3af4-b58d-55edc2a4c213 | -19.31739 | -43.81319 | 2025-09-28 03:40:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 17cc854b-100e-3dcd-87d6-51476514f485 | -21.44752 | -44.90302 | 2025-09-28 03:40:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 43fa15dc-3c12-3e14-88ac-867f820222ba | -20.08727 | -46.1669 | 2025-09-28 03:40:00 | NOAA-21 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e04dc9a-c79e-37d5-b28b-c2062cf6792e | -19.32868 | -43.82714 | 2025-09-28 03:40:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf201b85-fdf3-3efa-9868-74f58433b557 | -19.31644 | -43.81804 | 2025-09-28 03:40:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ec0f61c-e099-332b-950f-5dc51fb3bf5f | -22.9425 | -49.87691 | 2025-09-28 03:40:00 | NOAA-21 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 47040a5a-1324-30fb-927c-f49d3ab7530a | -17.76053 | -48.7508 | 2025-09-28 03:40:00 | NOAA-21 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 97a627dc-4609-3b82-81c8-68f763125003 | -20.41005 | -46.46924 | 2025-09-28 03:40:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65a263f0-7d11-341c-8eb3-7c9d4b081c50 | -21.79777 | -45.32526 | 2025-09-28 03:40:00 | NOAA-21 | CAMBUQUIRA | MINAS GERAIS | Brasil | 3110707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e3cf19ba-6784-3d15-9af6-7cbc8a3f1d27 | -19.32959 | -43.82246 | 2025-09-28 03:40:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4a83ec0-1206-3096-b40d-5e33c9cd0dc4 | -19.31548 | -43.82299 | 2025-09-28 03:40:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c30c05a-fb28-371d-a017-93103bc01893 | -19.86973 | -43.80528 | 2025-09-28 03:40:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| e56a39e2-07a5-3fe2-9cfe-3ea4b6fcc625 | -17.72712 | -46.69772 | 2025-09-28 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6c28cc1d-a09b-3a41-a793-e7df3d1a138f | -20.20736 | -43.05165 | 2025-09-28 03:40:00 | NOAA-21 | BARRA LONGA | MINAS GERAIS | Brasil | 3105707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a41c80ca-4d97-32e8-91aa-19dab1db9892 | -19.84808 | -42.59848 | 2025-09-28 03:40:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fa2d3a81-830e-3ee8-901d-fa49bb448448 | -19.66223 | -45.97342 | 2025-09-28 03:40:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 21e26b39-aca7-3b4d-b9ef-a94367bed9ee | -19.98953 | -42.341 | 2025-09-28 03:40:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b1a2683a-1fe4-31d5-b07d-ae39745fa6a8 | -22.94345 | -49.87679 | 2025-09-28 03:40:00 | NOAA-21 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 217d1495-2f05-36fa-a629-92a14be9ef97 | -19.9846 | -41.45377 | 2025-09-28 03:40:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f540e57f-e799-3f5a-a09d-32a3bb6efd9e | -19.9633 | -41.72608 | 2025-09-28 03:40:00 | NOAA-21 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 088db5d6-96ef-399c-8659-436a4a0f7f4c | -19.87055 | -43.80105 | 2025-09-28 03:40:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 4c7bd628-92e2-3faa-892c-8a2dacbcef33 | -23.15048 | -47.06092 | 2025-09-28 03:40:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 60f6e957-e840-354d-8cd9-907c80172ea8 | -19.31992 | -43.82414 | 2025-09-28 03:40:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c65b65e6-8718-38ee-8b27-e663b23cbe88 | -21.35637 | -45.78751 | 2025-09-28 03:40:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ad9b6930-88b9-351a-8f23-231037a19fc5 | -19.85706 | -42.59624 | 2025-09-28 03:40:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 60c59afe-ebe9-325c-8ff6-33426ab4d6e0 | -19.49844 | -44.26637 | 2025-09-28 03:40:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 872e9e6d-a532-3844-8adf-505f123b6969 | -19.32623 | -43.81575 | 2025-09-28 03:40:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a487c0f-0264-32da-93ba-00eebfc0a44a | -18.06411 | -42.3931 | 2025-09-28 03:40:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 14fd0667-a99b-3932-9b97-03b520c565d9 | -19.49577 | -44.25583 | 2025-09-28 03:40:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e721ead8-59f4-342f-955e-b56056ba5f44 | -22.05621 | -43.01984 | 2025-09-28 03:40:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6ecfd892-be22-389f-81ec-2c7ec7220b90 | -19.79867 | -44.04837 | 2025-09-28 03:40:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b1b3539-cf4a-3a87-8745-34935a13b0b9 | -20.41504 | -46.47133 | 2025-09-28 03:40:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0414d81d-d39d-3333-9864-f3c2a510b8a4 | -17.72634 | -46.7014 | 2025-09-28 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c6ffc277-fea1-31f9-b573-8338e90865fc | -22.06031 | -43.02048 | 2025-09-28 03:40:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2ffb4185-bdd9-384f-ae75-63988e12df72 | -17.24711 | -43.87032 | 2025-09-28 03:40:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7325da6e-f25f-3e06-b01d-e08b14ed015d | -22.06176 | -43.01297 | 2025-09-28 03:40:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c0892b1e-6b28-3be2-a14a-27ca5e60090f | -20.41429 | -46.47491 | 2025-09-28 03:40:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78eec5db-32df-356a-8841-04fe77a4d3ed | -21.07395 | -48.66373 | 2025-09-28 03:40:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7e22f18f-8713-3f1e-84fe-659f3b03c7bb | -22.73783 | -46.13067 | 2025-09-28 03:40:00 | NOAA-21 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0fb333e1-3a48-319b-8ff0-dae77c4a5576 | -22.90895 | -45.38993 | 2025-09-28 03:40:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 12fed82c-5cd4-3fdd-8e6f-e93732b7971a | -19.31104 | -43.82179 | 2025-09-28 03:40:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 898372d0-7979-3794-b26a-50a8a2c0a672 | -19.32373 | -43.80459 | 2025-09-28 03:40:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb37dd66-780f-3bcf-83f5-07ce20141f23 | -20.71242 | -45.01381 | 2025-09-28 03:40:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | MINAS GERAIS | Brasil | 3161205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6edb40c6-ba1a-3a3c-a825-08e43042541f | -17.7559 | -48.75767 | 2025-09-28 03:40:00 | NOAA-21 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 73ceb4a2-d15d-32be-9324-3d7e5cb83ae5 | -17.75693 | -48.76711 | 2025-09-28 03:40:00 | NOAA-21 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00a3d125-a277-32df-ad9d-17cfc3132489 | -22.06104 | -43.01668 | 2025-09-28 03:40:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 930baf51-dea6-3124-a0ff-4bcec60caf9c | -23.14976 | -47.06413 | 2025-09-28 03:40:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b10a1df8-1962-30e2-aadd-ba312bab7d3d | -19.24986 | -44.08501 | 2025-09-28 03:40:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74968088-7625-3590-9c4a-154e71848124 | -19.31833 | -43.80836 | 2025-09-28 03:40:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7c230973-53dd-315d-8ab7-0241975d4a6e | -19.3228 | -43.80938 | 2025-09-28 03:40:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93d2f65d-442d-31cc-a9e6-d296f245cfc5 | -20.20804 | -48.68433 | 2025-09-28 03:40:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 831983b7-5f63-3f1b-b9be-4d2e083390a7 | -19.86441 | -43.80886 | 2025-09-28 03:40:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 36d59aa9-cf84-3d84-91dd-f192a7756f03 | -19.96052 | -41.43325 | 2025-09-28 03:40:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b36f3b36-76df-3724-a807-fc8d47cc4ab2 | -17.72076 | -46.7003 | 2025-09-28 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8441853d-5cd6-3df8-a858-abc2f640b568 | -19.50859 | -44.26357 | 2025-09-28 03:40:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e09115b9-0e84-3ca1-b2ec-5d57844e1672 | -21.87711 | -45.29786 | 2025-09-28 03:40:00 | NOAA-21 | CAMBUQUIRA | MINAS GERAIS | Brasil | 3110707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 75d3fd19-ba63-325b-ab9c-28f6dc2afa69 | -20.40851 | -46.47648 | 2025-09-28 03:40:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7587b7bc-fb4a-34bb-8cdd-c2ca19befd9d | -19.20952 | -43.97505 | 2025-09-28 03:40:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b47193d-434e-3ec2-99b8-ffc97a6ad527 | -20.15548 | -41.5405 | 2025-09-28 03:40:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0d2b0d6e-9078-3db0-8e0d-9bd9808b9898 | -23.44024 | -46.69577 | 2025-09-28 03:40:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README24.md)
