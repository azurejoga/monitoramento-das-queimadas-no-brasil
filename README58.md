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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb0b7f7b-6471-3766-a87d-d5420f2a55ea | -9.82249 | -44.78821 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01f24283-c276-35d6-97ca-1619c9641ebe | -9.29024 | -50.31607 | 2026-10-07 04:21:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84e471b4-158e-34ae-83fa-8752d49f6fd8 | -8.81203 | -47.92228 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b7ddf63-b49c-358b-bdef-9860f7f2c1e4 | -11.05979 | -45.77602 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65c8c26d-53c0-365a-bca3-712df6cdc933 | -14.48476 | -47.07978 | 2026-10-07 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3eb840ed-b05d-318e-b0cd-96ca02ad388f | -9.87752 | -44.80473 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a55650bf-6938-375a-9d18-364e3dc5198d | -10.997 | -45.42868 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 77654a04-c6ae-3df2-8670-a32672d6b45d | -12.17122 | -44.71806 | 2026-10-07 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5799ac3d-f355-3b3c-bbd8-95808c896869 | -10.99423 | -45.42456 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| acdd4265-a5de-34db-8585-0f5c5274c0cc | -8.53734 | -55.37463 | 2026-10-07 04:21:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9a837e0e-c2a6-33fa-97ed-905cb87f444c | -12.95614 | -42.43393 | 2026-10-07 04:21:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bcffb000-18c1-360a-9aa9-69407585eb7f | -11.33041 | -46.67002 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 287f957f-d38e-3e0a-9989-d6950639a5cf | -11.75234 | -44.93759 | 2026-10-07 04:21:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 157d0889-2f07-34c0-bbd9-26b18922f822 | -9.87858 | -44.81935 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b831cd37-e58d-3927-844e-a11317b80fa7 | -8.98774 | -49.13352 | 2026-10-07 04:21:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32a330b2-bfc0-3d76-bb2b-f2b601667fe1 | -8.70473 | -45.20233 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7309feb5-2160-323f-845e-d622ab94eab9 | -11.22563 | -45.27541 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b45d4d6c-a096-31dc-b73f-7b4ff3b9997f | -11.10918 | -45.70586 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4bd3ad5d-d4b5-3d79-a3d9-da320fad3a36 | -16.03465 | -39.83103 | 2026-10-07 04:21:00 | NOAA-20 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 266ffd1f-89f7-3fd3-b3b6-e8965159aaa1 | -12.04311 | -43.3862 | 2026-10-07 04:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e5bc964-ac5d-351c-83ad-9fbf07591aba | -13.6818 | -44.28975 | 2026-10-07 04:21:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ebfcee50-256b-3185-b46e-a79b69cdb216 | -10.99976 | -45.43281 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ed30f827-3278-3d8d-8863-22699afdc399 | -15.42381 | -43.7058 | 2026-10-07 04:21:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 1b7cadc8-4af2-3623-8ba1-06d550eccf81 | -9.34458 | -47.84856 | 2026-10-07 04:21:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd04e775-64be-3dcc-a733-44cfbcb732ca | -10.99088 | -45.42406 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 0e545bc7-ae29-37bb-90d5-fa0e785a6f34 | -13.38599 | -43.87508 | 2026-10-07 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 228347e7-230f-39f2-ab7c-7eb1831eb063 | -9.80312 | -44.78145 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2250c057-bed9-3de9-96d7-45351ce09d79 | -8.9123 | -49.97138 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61211607-43af-3872-a5e5-e1d8894b26f6 | -9.90856 | -44.80254 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67191c46-e0ce-3ac3-aba4-a0e8967a7a0c | -8.69564 | -45.21568 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59a1940f-2ced-3d25-b482-32bf454fa82f | -9.45399 | -44.60614 | 2026-10-07 04:21:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4cd44b9-7dcb-3a14-8cd1-f4bfd4e5ff70 | -11.74515 | -44.94003 | 2026-10-07 04:21:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b332dcbd-a329-3671-b5af-626aaa63da9d | -11.37024 | -46.70884 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4ba3581-50a7-30d3-bdfe-98785c8564f3 | -8.70178 | -45.22041 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f917a44d-dccf-3078-a46e-35b2ee5930e3 | -8.92747 | -44.94441 | 2026-10-07 04:21:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 246a3d60-4e7f-3ce8-bda4-85dde00658b4 | -14.3332 | -49.85653 | 2026-10-07 04:21:00 | NOAA-20 | UIRAPURU | GOIÁS | Brasil | 5221577 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a18e41d-0ed9-38d8-a0b1-cba8b8c8f4e2 | -14.89018 | -44.81201 | 2026-10-07 04:21:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45dacbf6-f0a1-30d0-920a-530a2a88fffe | -10.857 | -50.66402 | 2026-10-07 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a29a76f0-8bdd-30e9-b4bf-5484f339b358 | -11.68083 | -43.62309 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a218abf4-ad41-393a-93f7-849e6b06c2eb | -9.92403 | -47.84789 | 2026-10-07 04:21:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8820ac57-2e11-39f9-aad8-b556bf316e8b | -10.37181 | -45.02653 | 2026-10-07 04:21:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52ef134e-1efa-3037-b3ac-a05d47dce2e7 | -9.89358 | -44.81093 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aeba8668-10ae-3585-8e91-191c2e8a048a | -11.36932 | -46.69285 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3c9ab1c-7c61-301a-a9d3-af4bc70cf5a2 | -11.07707 | -45.64857 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01d7dd8d-5f0a-368f-b336-6707b17f4047 | -11.23631 | -45.25164 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 114f8a33-0b66-3442-aabd-8f5986fd51a1 | -10.85751 | -50.68632 | 2026-10-07 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14029ade-6abb-3beb-bc22-4c50e62bc60a | -9.26674 | -45.64556 | 2026-10-07 04:21:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5004d6ef-f0d3-39d4-b45b-a66eb82166b3 | -13.00554 | -45.99868 | 2026-10-07 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0dcfc3e4-eff8-3993-80a6-d8a9b58a45a3 | -13.63185 | -43.68713 | 2026-10-07 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96761a39-6329-323d-bf3a-00262de6187b | -10.94254 | -45.39049 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea947b3f-d494-3bb0-a869-f0cab0778420 | -8.71087 | -45.20707 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 009398eb-a694-3722-b1cb-a2ff87430e7f | -9.51689 | -46.84399 | 2026-10-07 04:21:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04f6af77-d2cd-3b0d-b88f-c33a2dc10db5 | -13.20525 | -43.90517 | 2026-10-07 04:21:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dd45f8d-2249-3450-9fa3-822839346da7 | -10.14214 | -36.24534 | 2026-10-07 04:21:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 68282538-c09d-3433-b328-c9cb2b3de77f | -8.88213 | -45.37638 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 884625ca-92b8-3f82-853b-030bd1d1c1a1 | -15.72583 | -43.92923 | 2026-10-07 04:21:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b6e42c9-63d8-3be5-abb4-4244130733eb | -11.82845 | -43.54819 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c48d0726-5536-3319-bf79-98be2636382d | -8.88285 | -45.38028 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 896bb5f2-e8cb-3bbb-b38c-aa0d75ba6948 | -13.66905 | -44.30597 | 2026-10-07 04:21:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 929790bd-f3cd-344c-8129-b0aa2784960b | -8.74189 | -47.8791 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3bcf5bc4-e2e4-30e0-82c2-726b6b463b01 | -11.78762 | -46.58019 | 2026-10-07 04:21:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d034e688-21f3-3958-9168-a78c3c617de1 | -11.06555 | -45.82571 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64747a4c-0322-3c3a-9444-1f3877f096a8 | -8.71028 | -45.21069 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 58a57a9a-c196-38f4-b00c-45be0a1fe85c | -8.7081 | -45.20289 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 6ce10362-ed2f-3c53-b2fb-accebca364aa | -8.28028 | -50.27216 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ea780021-9a33-3ffc-9207-d18663774407 | -8.53119 | -55.38164 | 2026-10-07 04:21:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae21d865-cb2e-3db4-8d80-5c212b631ae1 | -13.58286 | -44.42319 | 2026-10-07 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b00c7b6a-d695-3a83-9e4b-49c234209e5d | -8.53642 | -55.37938 | 2026-10-07 04:21:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 51d91f71-7ba9-36ee-8785-79cbfa43c041 | -9.27039 | -50.66317 | 2026-10-07 04:21:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5b419f8-de1b-35b5-afaa-bd125bc1699c | -11.06433 | -45.76937 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38c8faf8-6e14-3cd5-9c82-e6d093aa7da7 | -8.69446 | -45.22292 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3de85d1-90ff-37ea-b3bc-c3df65d8ecd6 | -11.10859 | -45.7095 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cee690c9-d4a0-3655-a0b2-5c05a8d9aedc | -11.22793 | -45.26122 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b78b90c-28d4-3030-b5cf-23612dff777b | -11.09118 | -47.60178 | 2026-10-07 04:21:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0ec7765-65ef-38e2-9e7d-558da1e92f59 | -10.48302 | -50.42603 | 2026-10-07 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 48cdd442-fefd-3c82-aecb-775d6a75eaa5 | -9.96395 | -43.48807 | 2026-10-07 04:21:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8eed70b2-2f51-3fee-9b40-e0fc29a4179f | -11.7755 | -46.69612 | 2026-10-07 04:21:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc3e25d1-1178-3253-bd40-361c9b69a89e | -11.79556 | -46.70341 | 2026-10-07 04:21:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 11ece1e0-3bb4-32ab-802f-2629225ebfef | -10.2193 | -44.64377 | 2026-10-07 04:21:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 004aa95f-4ea7-3185-ab1e-163f50dc753a | -16.1448 | -43.51675 | 2026-10-07 04:21:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05995ca5-7b04-3e44-9f17-594d2ad13a66 | -11.06537 | -45.84815 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63d3696c-f006-3d6f-84c8-a0cf0a32904f | -11.73749 | -43.65395 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 791465ff-67a7-3f18-9a12-d6e7646bdcca | -10.06696 | -36.43286 | 2026-10-07 04:21:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4203654d-e094-3a80-b798-ed3e100ba12f | -11.37228 | -46.65319 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9036026f-8539-3133-bb47-c8b3da50538c | -10.29395 | -47.99807 | 2026-10-07 04:21:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b6e5219-524b-303d-bba1-a28dde40674a | -8.70414 | -45.20594 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 898542b2-7e6f-3297-8c1d-f89a6a972002 | -9.26734 | -45.64183 | 2026-10-07 04:21:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f395924c-59b7-34ee-8449-455198c1376f | -9.79666 | -48.92008 | 2026-10-07 04:21:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3041f54-c659-3208-9022-52183f3e1b13 | -9.25077 | -45.658 | 2026-10-07 04:21:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d178303-10fd-35fc-81ba-dfbd97895e72 | -11.3788 | -46.67841 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cacdaa8d-f63a-3046-b349-521a161a9f5f | -13.50384 | -44.36293 | 2026-10-07 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2432b4c1-0640-34a4-b96e-74cf2efb8ad2 | -9.90468 | -44.80553 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d42903b-ffc5-3dbc-bea9-787d55bc7593 | -11.60981 | -44.14406 | 2026-10-07 04:21:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6c0269ee-5fdb-3424-8601-b96202a95d18 | -8.38669 | -48.0743 | 2026-10-07 04:21:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c610cae-1975-3532-aa11-2b5bf5a1acdc | -9.81917 | -44.78767 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89d1b32b-63c5-356b-8ea8-909a434029cd | -10.97315 | -45.40644 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eef62959-6ec2-34e4-9b2d-5c6976e6aaaf | -13.86227 | -43.75723 | 2026-10-07 04:21:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 294d5f8e-c954-312c-a8f1-6f89196dea3b | -11.84125 | -43.55387 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae5e37ae-d608-3be1-8d1a-02cb66164716 | -8.7144 | -45.1854 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3cc7899e-66a0-3583-bb3d-7d2a85871c0a | -9.35542 | -45.42716 | 2026-10-07 04:21:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README59.md)
