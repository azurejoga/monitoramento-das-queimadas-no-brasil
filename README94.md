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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4dba249d-4bf9-34a2-a912-8a9a6079d6b2 | -6.18653 | -43.99031 | 2025-08-30 12:14:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 51262ff5-aabb-31bf-8d28-1f928c8786ac | -6.24216 | -41.81897 | 2025-08-30 12:14:00 | TERRA_M-T | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| c5b5b90f-33ba-335a-b8cd-c1264d5b92c9 | -5.87961 | -42.97014 | 2025-08-30 12:14:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 8a798f29-10ab-314b-ae7f-13262b932686 | -8.86991 | -45.7384 | 2025-08-30 12:14:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 48.5 |
| a4fbf0f2-f2c0-354e-89f4-b23b5c01a91b | -6.56078 | -43.68101 | 2025-08-30 12:14:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e7453b7a-2e67-38e0-9c02-47bb3bc955dc | -6.23645 | -41.81183 | 2025-08-30 12:14:00 | TERRA_M-T | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| d169578e-035f-3b15-8004-54b4f385f08c | -7.85209 | -46.97522 | 2025-08-30 12:14:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 235.6 |
| 95d44a18-c1dc-3bf3-8865-0cb41c767f8f | -6.84383 | -42.81564 | 2025-08-30 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 5c6e30b4-8c14-3b43-b889-830fe6f0b69e | -6.17523 | -44.20055 | 2025-08-30 12:14:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 61cbe2ad-dde7-3fc3-bd67-4ae4ed1e13fe | -7.21545 | -45.44881 | 2025-08-30 12:14:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0b7ac078-30be-3f07-941d-bbd0a4603f07 | -7.783 | -45.47476 | 2025-08-30 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 6d86b4c0-cb14-36e9-9c16-778bee7debdf | -7.23222 | -44.21799 | 2025-08-30 12:14:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b9196159-6df2-338f-8cbc-10eceb606842 | -6.48645 | -44.41035 | 2025-08-30 12:14:00 | TERRA_M-T | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8992dc44-e630-3fe0-8ae2-bf95da9bea60 | -7.2168 | -44.05945 | 2025-08-30 12:14:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0b17a74d-5f0c-396d-9581-f4e71476e2a2 | -6.52533 | -44.84997 | 2025-08-30 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aba3ceb7-3733-3454-872c-efa1e84ea64c | -7.22576 | -44.19742 | 2025-08-30 12:14:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 66100491-e9c3-396b-a9f5-37780590c332 | -6.77816 | -43.78291 | 2025-08-30 12:14:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 53.7 |
| c31e4879-a7c1-35f4-9498-4159980add5a | -7.32346 | -44.08998 | 2025-08-30 12:14:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d8c96193-7663-33ff-adb6-5ce23bf659eb | -7.85342 | -46.96615 | 2025-08-30 12:14:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 8a02d19a-911f-3d7a-8c66-1ece4a170f89 | -9.1117 | -46.04548 | 2025-08-30 12:14:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 950d3f07-ec43-3f46-9ad9-a36ccacabd72 | -6.4184 | -45.5966 | 2025-08-30 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| b1e9c1bd-9137-37d6-842c-87361894d3b2 | -2.95708 | -42.85322 | 2025-08-30 12:14:00 | TERRA_M-T | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| f18dde4e-675b-3456-9453-f97adbe8677b | -3.48133 | -39.10226 | 2025-08-30 12:14:00 | TERRA_M-T | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 109.9 |
| d23f22f2-8fe5-3cf8-8566-aeffaf4e4a35 | -6.16679 | -43.3402 | 2025-08-30 12:14:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 100e5f4f-64f4-3cc3-bf3c-a2377fde0504 | -8.01013 | -44.05846 | 2025-08-30 12:14:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 266720c7-09e2-3b8b-9a7c-b95c8e6677dd | -8.87153 | -45.07709 | 2025-08-30 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ce17b094-255d-3320-9e79-5ecc1a15960e | -6.82168 | -43.33618 | 2025-08-30 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 30.6 |
| a6907929-300c-32c2-b688-6f8e0dd5cb15 | -6.48791 | -43.54279 | 2025-08-30 12:14:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 6593870e-a7a9-3781-b7e3-17b16f5d3bfb | -7.85076 | -46.98433 | 2025-08-30 12:14:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 3f2ddb5d-d15a-3cd6-a2d5-9392e0b24217 | -5.61889 | -45.00531 | 2025-08-30 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 547d15e1-2e3c-3d1c-ba0d-c6394864d6c7 | -6.8312 | -43.33754 | 2025-08-30 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 58.7 |
| d925912f-db7b-37f2-8e7e-1b7be0dc26d4 | -9.8379 | -44.6868 | 2025-08-30 12:14:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 99a04224-27f3-3f17-becd-491a44adbfab | -9.66918 | -45.95261 | 2025-08-30 12:14:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 3f39da7c-169c-317b-9942-6ad89a6917b8 | -6.94775 | -42.80153 | 2025-08-30 12:14:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| fecfad4c-8f31-3b89-aeef-0d1c8a31ac7c | -6.30983 | -44.4206 | 2025-08-30 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5db7a3a6-a4b5-3502-bd2e-93fa65071928 | -6.59434 | -43.64494 | 2025-08-30 12:14:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 12d2ab62-a30f-3376-a3e3-72520315c760 | -6.70504 | -43.08913 | 2025-08-30 12:14:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 71ed6267-ba68-3e8d-bce2-8086ff556d2f | -7.09819 | -44.31866 | 2025-08-30 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 8b22c54d-7027-38a4-a152-35dfa5e7fcb0 | -5.26597 | -43.19705 | 2025-08-30 12:14:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b5cf47eb-62ed-36ac-98d5-8c832aeb5161 | -7.60319 | -42.7133 | 2025-08-30 12:14:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| abf2e7a6-95cc-3043-b49e-e1b17e004157 | -3.48591 | -39.09081 | 2025-08-30 12:14:00 | TERRA_M-T | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 24.9 |
| f85814cd-05e1-3ced-96fa-63b60f136b31 | -9.11941 | -45.21457 | 2025-08-30 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ab0211ab-ae5c-3fcf-854c-7c029967dd42 | -6.65603 | -43.92891 | 2025-08-30 12:14:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f4b8fd30-41b1-31eb-9f42-ce5e6daf901a | -7.44282 | -44.81691 | 2025-08-30 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 3040757b-516a-3c25-b84f-a65c9f5876a6 | -6.21661 | -42.76614 | 2025-08-30 12:14:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| e260f39b-230f-38f0-8232-fc8b738e4cf8 | -6.20831 | -42.75386 | 2025-08-30 12:14:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| f142fdf6-5d99-3f29-bbb4-b80d5cf18b5a | -4.06933 | -42.5359 | 2025-08-30 12:14:00 | TERRA_M-T | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| c549e583-421b-3f8b-b687-8f62b58cd8f2 | -4.5948 | -43.31599 | 2025-08-30 12:14:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 1e384f2e-829e-3dd9-8934-ff06426ea22f | -7.4441 | -44.80784 | 2025-08-30 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 415a60d7-2233-3297-ada5-58d0eba117a2 | -6.834 | -42.81427 | 2025-08-30 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 29.5 |
| edaa429b-051b-31a8-abd5-3be62da250c0 | -6.95286 | -44.30541 | 2025-08-30 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 42231660-8265-3d37-bf8d-c2729333d34d | -6.37643 | -44.34134 | 2025-08-30 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| eee2f5f8-dbca-3929-81cc-70e8ce7e7899 | -4.09922 | -42.46383 | 2025-08-30 12:14:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| aa1a154f-1ab0-3527-b675-7f24ed7f6c55 | -6.36329 | -43.57091 | 2025-08-30 12:14:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b8017b09-b030-3c4e-850f-c640dbc94720 | -7.21671 | -45.43993 | 2025-08-30 12:14:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3cfbac4d-6c13-3052-a4ea-be1f39acb144 | -7.90953 | -45.16915 | 2025-08-30 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e6ba111e-00dc-3f38-8e41-b60a2543e18d | -6.65467 | -43.93857 | 2025-08-30 12:14:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e9241a98-444c-3a92-a181-932242ec0221 | -6.09621 | -43.32455 | 2025-08-30 12:14:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 66a9b827-ae7a-3242-a207-3ed7f5f46bae | -7.15346 | -44.90691 | 2025-08-30 12:14:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 61593f27-4ad6-33e7-9cfc-dff7359fa4e7 | -6.13691 | -43.94461 | 2025-08-30 12:14:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 642f8ee9-da62-3608-9ff0-d08c935e6f1f | -9.41321 | -48.27356 | 2025-08-30 12:14:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 971d84d3-457f-3541-a6ec-42c3a3f3ad46 | -3.361 | -43.37138 | 2025-08-30 12:14:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fe6ff141-911a-3e01-9381-1875ecaaf4ba | -6.28527 | -44.46423 | 2025-08-30 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 743655d3-ecd5-367a-a621-270453c4aef9 | -8.39943 | -44.96196 | 2025-08-30 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 6266f490-ebfb-355f-bcd6-d04f31844233 | -9.41469 | -48.26371 | 2025-08-30 12:14:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 827d5d6a-5503-3348-b16e-922672e448f0 | -6.76887 | -43.78165 | 2025-08-30 12:14:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 0a9081c3-0a64-3bf9-a68b-c883f722c708 | -6.11113 | -44.72138 | 2025-08-30 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fdd113c3-0da8-38de-898f-609cbab411ec | -6.10999 | -43.2952 | 2025-08-30 12:14:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 10.2 |
| cafd0055-10e7-31ce-b466-b215abd2a315 | -6.50663 | -43.54557 | 2025-08-30 12:14:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 59796c72-e791-3953-a65b-db2e0ca53270 | -9.13785 | -49.61874 | 2025-08-30 12:14:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f3188925-ed44-346a-b460-ecafcf5da59b | -6.18713 | -43.33256 | 2025-08-30 12:14:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 1d503db5-8edf-3744-8ad7-5d8e2749371b | -6.59573 | -43.63503 | 2025-08-30 12:14:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2d3d7eba-1329-3874-badc-efc7643e333b | -6.77955 | -43.77307 | 2025-08-30 12:14:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 54.2 |
| a2b85265-bd06-3ac3-8488-95e3fb8f2d9a | -6.31115 | -44.4113 | 2025-08-30 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ab0f2eb2-025c-31ae-b831-c17143bfacac | -8.11677 | -45.00671 | 2025-08-30 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6e583258-81a1-3d52-bc72-3532a275277f | -6.16637 | -44.13252 | 2025-08-30 12:14:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 744a41bc-7960-38b2-8540-84403b7e885c | -9.67675 | -45.96284 | 2025-08-30 12:14:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 262b39a9-dcc4-3957-b272-6472688d3fb9 | -7.01358 | -42.02188 | 2025-08-30 12:14:00 | TERRA_M-T | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| dce13096-911b-3d49-839a-1ed3dd080cb4 | -6.83249 | -42.82547 | 2025-08-30 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 0ad91691-5f53-3773-a785-165efa4911f7 | -2.96237 | -42.86033 | 2025-08-30 12:14:00 | TERRA_M-T | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 5f41e3f8-f66f-3b70-845c-965f4c71f32a | -8.08182 | -48.40839 | 2025-08-30 12:14:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 7eea1ea2-3e7e-349a-94bc-02c09b503b21 | -7.11581 | -44.58757 | 2025-08-30 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6efaa397-7a7c-3069-b068-0658fdd51de9 | -7.42616 | -44.80531 | 2025-08-30 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 47b863ce-7763-35aa-8fa2-15a6ad399496 | -7.25086 | -45.45371 | 2025-08-30 12:14:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 4479a617-b95b-3e4b-9035-5b085c75040a | -5.8397 | -42.52727 | 2025-08-30 12:14:00 | TERRA_M-T | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 6436ac0c-27b2-3109-9c50-a02b45ec73d6 | -5.76257 | -45.22739 | 2025-08-30 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a29d9a5f-a71e-34dc-8f40-66827e17d34f | -6.83157 | -42.81882 | 2025-08-30 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 40.5 |
| c031fbaf-f087-34f4-bfba-b4ca1638a170 | -9.83924 | -44.67715 | 2025-08-30 12:14:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 82aa931b-c40a-3d4c-ad0b-24506a1626c8 | -6.76851 | -44.63358 | 2025-08-30 12:14:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 0e48da77-4418-334b-905c-74d0fe86c69b | -7.22601 | -44.06078 | 2025-08-30 12:14:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 03096e43-efb8-36b4-a7a2-bcfb76c3a306 | -6.10565 | -43.32589 | 2025-08-30 12:14:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8643cbcc-b891-3b6f-8358-053c7bf85e6f | -7.22145 | -44.75505 | 2025-08-30 12:14:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 24e3da6e-6398-347c-85ba-a7d2bcdd0dc6 | -8.40072 | -44.95278 | 2025-08-30 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| e9c66f1b-5bb5-3556-8651-d4fdc13c325e | -3.78959 | -41.75739 | 2025-08-30 12:14:00 | TERRA_M-T | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 7ce50c8c-8adf-3251-ab60-49f0a9070f16 | -6.17767 | -43.33131 | 2025-08-30 12:14:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 0ba8cecb-f197-37ba-bdd4-d8b2d0f49125 | -6.28265 | -44.48267 | 2025-08-30 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| aa2f25ff-c8a5-335b-80e8-d2a593f79448 | -6.49588 | -43.55418 | 2025-08-30 12:14:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 94f9f02b-a5a7-3009-b495-63be09a9a086 | -6.49727 | -43.54417 | 2025-08-30 12:14:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 361af0fb-7476-30f3-a25c-c8a3f3cd0026 | -7.22274 | -44.74591 | 2025-08-30 12:14:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 2f186f89-0575-3b22-865c-52e015595f38 | -7.11905 | -44.76266 | 2025-08-30 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |


[Clique aqui para ver as próximas entradas](README95.md)
