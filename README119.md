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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 588df858-447d-39bc-ba3d-8e07eecf80c3 | -8.3832 | -48.3099 | 2025-09-03 14:00:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 98235a51-e7fe-3159-a712-f9c894ac64d5 | -7.7226 | -48.7355 | 2025-09-03 14:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 77175d84-1237-399e-ac72-0ac4e16c3e9a | -7.7039 | -48.7371 | 2025-09-03 14:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 121.2 |
| f402c0f9-a2ab-3af7-bbcf-367b903028cc | -6.6982 | -48.4035 | 2025-09-03 14:00:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 8d990197-ef72-3540-8e3b-777b2fb46036 | -7.484 | -44.8272 | 2025-09-03 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 6f2119c9-6f84-3600-b1a7-f533bb94496b | -6.35 | -45.6723 | 2025-09-03 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 73941c62-5d1e-3d53-9be5-d4ee3260efd0 | -7.7036 | -48.7587 | 2025-09-03 14:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 48d5c4d1-4fc4-323b-a1da-01522ed6b6f5 | -6.7967 | -44.1091 | 2025-09-03 14:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 46ecaebf-7826-3f38-b09b-ba4f30639d6b | -14.5655 | -53.0503 | 2025-09-03 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| e31f9a00-8d06-32eb-a67d-8dc1f1c914bb | -7.7224 | -48.7572 | 2025-09-03 14:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 182.5 |
| 75251683-0444-3488-8c39-6227f03ce34d | -5.7738 | -45.2865 | 2025-09-03 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 80e3e3d2-29d1-3813-b136-ee8424317c8b | -5.8882 | -42.9988 | 2025-09-03 14:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 119.9 |
| c235bbdb-70f8-31ca-829a-bfacac22b352 | -6.7407 | -45.911 | 2025-09-03 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 660eb4e9-4177-3ca9-9200-82d0f558bee8 | -11.2005 | -55.0195 | 2025-09-03 14:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 7cf3c3f8-4433-3405-967f-62f5a41da073 | -11.672 | -52.168 | 2025-09-03 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| fe77168d-fa07-3adf-93c9-39e2ba20da81 | -10.0932 | -54.7667 | 2025-09-03 14:10:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 157.2 |
| 3b5df425-f602-3137-a7e9-2f38f08c48e5 | -7.4969 | -45.3495 | 2025-09-03 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 9b8505d8-8340-3c1b-9cd3-8779fe76dffe | -11.6156 | -52.132 | 2025-09-03 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 675821c1-d6f1-39a7-8fad-f63e0962fedb | -8.0605 | -45.3863 | 2025-09-03 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 0c84dbaa-fc44-33b9-b7aa-dd17e45d9aed | -11.8843 | -50.6197 | 2025-09-03 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 6bff0646-da9f-3031-99a9-c9a041e84708 | -10.4816 | -53.6527 | 2025-09-03 14:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 06e03fcd-180c-3a66-be32-cdb02b9fa291 | -7.0128 | -43.2525 | 2025-09-03 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 354580e5-190b-3291-8d32-c4ae8138b4be | -7.7226 | -48.7355 | 2025-09-03 14:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 144.3 |
| 4d81cc91-fab0-35ad-aeeb-e308a49b277b | -8.0794 | -45.3844 | 2025-09-03 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 155.1 |
| c445e2de-f761-3eb1-b243-2307f9c4214e | -5.2575 | -44.4581 | 2025-09-03 14:10:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 3d60a5a3-1674-3d5d-9efd-b588600a850b | -11.5966 | -52.134 | 2025-09-03 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 123.3 |
| cb67dbca-af68-33c3-9141-b2890bbf85c7 | -9.6226 | -47.0861 | 2025-09-03 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 153.6 |
| afc13450-b4cf-301e-ba23-aaa7ddf99973 | -16.3145 | -52.9628 | 2025-09-03 14:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 36c3ba70-c5dd-3990-aa97-68c4224b4607 | -11.6836 | -57.3518 | 2025-09-03 14:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 170.1 |
| 9c7aa5a1-4617-35f8-b27d-c9165773db3c | -6.7407 | -45.911 | 2025-09-03 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 5e107b54-96ef-3a70-bc7d-61775b2632c9 | -5.7154 | -45.5613 | 2025-09-03 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 6103c8e7-1eec-3725-a0c1-beb85874e4a2 | -6.6213 | -53.1536 | 2025-09-03 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 460fad90-b5c7-3f4d-887a-c01359926841 | -7.5487 | -47.4647 | 2025-09-03 14:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 57d4648b-d9a8-3f9d-aa5d-d1eb5c1b46a7 | -11.0249 | -47.121 | 2025-09-03 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| bdd4a524-c09b-3c49-afea-431e70c9dde7 | -7.549 | -47.4427 | 2025-09-03 14:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| e876b202-b5dd-3a0a-ab8b-c2b06d9344be | -11.5969 | -52.113 | 2025-09-03 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 159.4 |
| 082c726d-3835-3ddd-8b09-d9a0743b334c | -15.1771 | -52.356 | 2025-09-03 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 7abd9c00-345b-3a15-b14e-3d77e0c54294 | -10.9509 | -50.8722 | 2025-09-03 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 14f87ab7-bf0a-3818-a0d6-e8e99e0841ae | -6.3502 | -45.6498 | 2025-09-03 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| bcd8b5ca-1e79-32ac-baef-493ab1623bea | -8.0203 | -44.0608 | 2025-09-03 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 63ce4e32-85e9-30e3-827e-1494d67fd4e4 | -12.793 | -47.6415 | 2025-09-03 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 7f675d2c-317b-3884-880e-165d18eb3a49 | -6.8569 | -45.5415 | 2025-09-03 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 83248e74-4b33-3d3e-8a2b-1ecfdf192712 | -5.7923 | -45.3078 | 2025-09-03 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 45044de0-a0e4-3356-aa91-115e8e613d1a | -7.5157 | -45.3478 | 2025-09-03 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| cbc39c48-2a93-30e3-9ef5-4d308e8aaf12 | -9.6232 | -47.0416 | 2025-09-03 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 81bf0956-fab4-341c-a586-50e4cd421153 | -6.3689 | -45.6483 | 2025-09-03 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 4c9b8587-83fc-31b9-b011-5405609379ad | -6.8465 | -52.8337 | 2025-09-03 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 60bc50ae-2fd6-3624-a265-cfb336f9bc4a | -8.2006 | -49.5559 | 2025-09-03 14:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 187.0 |
| 2370fc74-bcda-3a46-88ec-afa80193eef0 | -7.4966 | -45.3722 | 2025-09-03 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 121.3 |
| c0ff5fbf-0d07-3962-aa0e-b8e4c6ac52bf | -11.9635 | -45.7741 | 2025-09-03 14:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| f924b850-7aab-375f-b315-c7151aec74c3 | -10.463 | -53.6338 | 2025-09-03 14:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| c8e2bb21-2d1e-37cc-809f-11312a337d0d | -15.737 | -53.635 | 2025-09-03 14:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 177242e2-8ebd-3469-aa26-ed924e21e77c | -9.636 | -46.1221 | 2025-09-03 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| a74cd535-05c4-35ea-bf27-0df4a56051b2 | -8.0796 | -45.3617 | 2025-09-03 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 261.7 |
| 08287b2c-5c7c-3b0c-a6ca-4d4284c2a6c2 | -6.0699 | -45.6259 | 2025-09-03 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 156.3 |
| eeba87de-6c54-3b7e-9bd2-2fc15d0a7f79 | -7.7036 | -48.7587 | 2025-09-03 14:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 0c3c30f3-daf4-3152-ac2b-7d6a82e14940 | -7.4842 | -44.8043 | 2025-09-03 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 96ed03cf-0e49-3e5a-a5ab-722c2efa4c78 | -9.1373 | -49.6659 | 2025-09-03 14:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 8f16bc20-f278-3dfd-ace4-07e403fa5727 | -7.302 | -44.2936 | 2025-09-03 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 985e7bcc-728e-31f5-8f75-85d42656cedc | -7.6851 | -48.7386 | 2025-09-03 14:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 71.0 |
| ec3fc4a5-4c7e-380b-a045-279e9febdf9e | -5.7738 | -45.2865 | 2025-09-03 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 180.2 |
| 1170365d-f1ef-342d-9fce-ba7171a111eb | -7.7224 | -48.7572 | 2025-09-03 14:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 166.0 |
| 873ef176-416d-3ef9-9c03-5454388bbaf6 | -7.3209 | -44.2919 | 2025-09-03 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 6947672e-85c9-367b-a13f-73561fe38093 | -11.8533 | -51.4318 | 2025-09-03 14:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 101013c3-ad23-340c-a71c-749a37dc8ce0 | -12.7926 | -47.6638 | 2025-09-03 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 50e4c834-7e5b-303a-b3e4-71f844549df6 | -8.8842 | -45.822 | 2025-09-03 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.2 |
| c0b7789d-a9f6-390f-85df-ab59c0d474dc | -6.2221 | -43.3927 | 2025-09-03 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 229.3 |
| 2676be20-a30b-3794-bfa0-ac0c44d486d7 | -5.8882 | -42.9988 | 2025-09-03 14:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 195.2 |
| 97dd1064-2f82-3268-93c8-05a84cd423a2 | -14.4071 | -53.3013 | 2025-09-03 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 5ea3019f-dd96-3333-ab17-937e4c14b34e | -8.02 | -44.084 | 2025-09-03 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| b7672fac-dece-3698-a17d-a50763574197 | -8.3646 | -48.2899 | 2025-09-03 14:10:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| f6b2a60b-0138-376a-89fe-47df3b03b842 | -6.6982 | -48.4035 | 2025-09-03 14:10:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 259f0e68-26ed-3fad-93af-a1866272c4a5 | -6.797 | -44.0859 | 2025-09-03 14:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 9e1a4702-d0f4-3b99-ba05-eb27b4940974 | -7.53 | -47.4662 | 2025-09-03 14:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 141.9 |
| b1648847-b894-380e-8ca5-bf43f338cf63 | -5.7343 | -45.5375 | 2025-09-03 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 111556ed-82be-3219-b52d-5534a57ce6d2 | -8.8278 | -45.8054 | 2025-09-03 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 1f9c3aa0-332f-3c3e-b99d-74afe73c7402 | -11.6647 | -57.3533 | 2025-09-03 14:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 4c925878-ab27-31b1-ac30-14302579dd95 | -6.7967 | -44.1091 | 2025-09-03 14:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| d396874a-3b4d-3dbc-9da3-a1585ce24bc2 | -5.7181 | -45.2453 | 2025-09-03 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 298.3 |
| 54d7487f-5a28-39e9-9143-84027fb4c271 | -6.8466 | -52.8132 | 2025-09-03 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 5e32173d-3178-3519-9bd2-d64c08a1c4bb | -10.913 | -50.8762 | 2025-09-03 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 3db68f83-9705-3d04-b7cd-4d8f23ae7485 | -11.9034 | -50.6175 | 2025-09-03 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 767715b0-6221-3552-99af-c04236371e43 | -9.6229 | -47.0638 | 2025-09-03 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 3eb4550b-81a0-310f-860c-683139ce8ed9 | -12.9189 | -57.0074 | 2025-09-03 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 06750e44-7c46-35f3-99e3-02df9118d252 | -8.8839 | -45.8446 | 2025-09-03 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| febff3bc-367f-3058-bf39-3f07d21b154d | -6.0966 | -46.8281 | 2025-09-03 14:10:00 | GOES-19 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| e56e50f5-f046-3fc2-abcb-5ef9b44fc159 | -8.0723 | -47.5946 | 2025-09-03 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| f440ae9f-c65b-386b-b4fa-2f9adbfbd177 | -8.3644 | -48.3116 | 2025-09-03 14:10:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 39e27a32-21d7-3e5c-a256-64db949f9e4a | -6.7595 | -45.9095 | 2025-09-03 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 182.7 |
| 03ac0f96-eb25-36d8-be00-23fe549db50b | -6.2036 | -43.3709 | 2025-09-03 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| e54400fd-4bd8-31a5-b97f-51f23e50fc04 | -10.4818 | -53.6321 | 2025-09-03 14:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 04ec2717-d622-33cd-bb60-f24e2ac74367 | -6.7928 | -44.4776 | 2025-09-03 14:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 06e172ca-8f36-3188-bdd1-a696ccbc6cc0 | -5.8642 | -45.6408 | 2025-09-03 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| c583a075-77ee-3267-ad9a-85cb6ef0a2c7 | -7.7039 | -48.7371 | 2025-09-03 14:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 129.3 |
| bed9ce63-2a3a-39ed-9115-8a6d359158bd | -6.2224 | -43.3693 | 2025-09-03 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 252.4 |
| c9ebcb31-4b54-3281-9c99-55278e514933 | -6.2038 | -43.3475 | 2025-09-03 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 99182e4b-94c2-3ddb-9632-584c9402d10c | -11.0181 | -51.5001 | 2025-09-03 14:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 110.3 |
| c6637aa4-7460-3ede-a2de-13cfe507bc6f | -5.8884 | -42.9753 | 2025-09-03 14:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 243.9 |
| 7cb8ff7d-9b2d-369d-8562-ed38186823c7 | -8.0608 | -45.3636 | 2025-09-03 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 190.2 |
| 3e4c1476-b9d7-3490-aea9-7f3d6140651e | -13.5167 | -47.0167 | 2025-09-03 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 76.1 |


[Clique aqui para ver as próximas entradas](README120.md)
