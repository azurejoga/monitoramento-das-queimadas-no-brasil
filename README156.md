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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b3ea6cb-6506-3f8f-b27b-71fe5b48e08e | -1.4302 | -48.9955 | 2026-09-22 16:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| b83f4758-209d-3f42-baf1-25c18abbaf30 | -3.0352 | -61.277 | 2026-09-22 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 64dfc31a-9b37-34cb-9293-870eb8e92472 | -2.9997 | -60.8047 | 2026-09-22 16:10:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 51c23b71-ec98-3240-9063-8a0da9651dbb | -3.6449 | -58.8647 | 2026-09-22 16:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 07f5737e-695f-37ae-b271-1e601ccb90b7 | 1.3634 | -56.0834 | 2026-09-22 16:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| e145c66d-d012-32a5-ba58-e12ea50edcc2 | -6.0196 | -51.7893 | 2026-09-22 16:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| d257784a-2e6d-3983-92f6-7bb79ea03f22 | -2.7713 | -57.0229 | 2026-09-22 16:10:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 8d6b3475-a95f-3924-b2ac-dd228ffeb755 | 1.3634 | -56.0638 | 2026-09-22 16:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 7733d656-a7df-3394-9262-a041321fb959 | -1.4487 | -48.9526 | 2026-09-22 16:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 559c5dc6-a0d4-3987-8f5e-59e20b429dd4 | -3.6632 | -58.8643 | 2026-09-22 16:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| a43347df-1ebf-3a52-bcdf-86c8eb72a61a | -3.1851 | -59.6982 | 2026-09-22 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 6d62334b-4525-30c6-b080-f34a2aa6d6e9 | -9.257 | -46.1873 | 2026-09-22 16:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 535706a1-de9d-3b34-97ef-df56d00814cf | -3.2189 | -60.8011 | 2026-09-22 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 1280589b-2f5c-3a51-a766-6fef65fb5830 | 1.4269 | -50.7657 | 2026-09-22 16:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 8854c7f4-19d2-3dec-b91e-dcc13d6e59ae | -9.7693 | -46.0615 | 2026-09-22 16:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 1723b60d-525f-3a73-86eb-df1af1bc6643 | -11.0048 | -49.7325 | 2026-09-22 16:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 149.2 |
| c9d775bb-1750-36d8-b78b-f78794cd83e0 | -6.9 | -41.72 | 2026-09-22 16:15:00 | MSG-03 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 89d7d1d7-2ac6-3a50-afc0-809c48b36520 | -15.81 | -42.05 | 2026-09-22 16:15:00 | MSG-03 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d508f8fa-7362-35cb-9aca-ce645e1e3a7e | -10.55 | -43.96 | 2026-09-22 16:15:00 | MSG-03 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f3bad036-c29f-37d0-9a0f-f23e43358c4d | -11.74 | -50.99 | 2026-09-22 16:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aaa0af11-75e9-355c-b864-a21316132940 | -6.23 | -41.63 | 2026-09-22 16:15:00 | MSG-03 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d20d633b-0dfd-306b-b737-8c3ff633aa30 | -6.23 | -41.68 | 2026-09-22 16:15:00 | MSG-03 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dd359685-22f3-3f76-943f-066133c8d317 | -9.61 | -43.94 | 2026-09-22 16:15:00 | MSG-03 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d172f20a-d166-3054-92e8-fbdfc5fadd19 | -6.21 | -41.67 | 2026-09-22 16:15:00 | MSG-03 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 994129fc-d870-315b-aea7-cf2a6ca71d89 | 2.2003 | -50.8773 | 2026-09-22 16:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 82.1 |
| dab0571e-4e41-35be-a43a-91bd67c35714 | -9.788 | -46.0819 | 2026-09-22 16:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 5807ecef-00f3-356e-87c9-f9fd23169bd3 | -10.7715 | -46.3001 | 2026-09-22 16:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 526efa9c-a965-3b99-95ec-b9014579c5b8 | -3.3134 | -59.6003 | 2026-09-22 16:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 8d830ce4-6452-38bb-a08e-667e6d299bac | 1.9497 | -55.8992 | 2026-09-22 16:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 51750c38-8d4f-3720-8957-29eb73fb073f | 2.2187 | -50.8769 | 2026-09-22 16:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 83a4d9b5-e4de-36a3-877c-1efabcd9519f | -2.5687 | -57.494 | 2026-09-22 16:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 8821fc0a-f523-3657-b3d3-cf5c083bbc18 | -1.0244 | -48.8087 | 2026-09-22 16:20:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| e74484f7-620f-3e8a-b089-e30c4bc36f22 | -10.4297 | -50.2663 | 2026-09-22 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| f3e65410-0337-350c-8417-f076368ff7f2 | -1.4302 | -48.9955 | 2026-09-22 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 93c6364b-c39c-35b0-8718-4820330c6746 | -3.7313 | -60.5638 | 2026-09-22 16:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 5aa57ff6-0d20-37e4-958e-d52ef067916f | -11.3784 | -44.2195 | 2026-09-22 16:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 03451dd1-fa24-34f1-a038-7d388802e0ce | 1.5287 | -55.7468 | 2026-09-22 16:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 0b7ddf0d-769f-3971-b04c-9687842c8657 | 1.3817 | -56.0636 | 2026-09-22 16:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| d617c7a9-551e-3a49-9db6-644b838cb133 | -10.4475 | -50.3499 | 2026-09-22 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 27317aaa-cd9b-3fe6-a77d-7b69065e0da0 | -10.3171 | -50.2138 | 2026-09-22 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 5fb206ae-b9f0-32e9-a04d-353d8689e58c | 1.5836 | -55.7856 | 2026-09-22 16:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| b1fb22ff-b607-3c1b-875e-656454456b98 | -1.4302 | -48.9529 | 2026-09-22 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 849f35e9-8226-37c8-a469-5e965456d183 | 1.4269 | -50.7657 | 2026-09-22 16:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 72.5 |
| d732315c-d2af-310c-9860-825ec49973f8 | 1.4453 | -50.7655 | 2026-09-22 16:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 79.5 |
| e78a9432-5cfd-304c-a279-96e7783d6d53 | -6.0928 | -57.6262 | 2026-09-22 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| b2df5051-30c1-3cb2-81e7-10ebd5ac52e4 | 1.547 | -55.7466 | 2026-09-22 16:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 8ac3e8b6-8c18-385e-aefb-4c56c8453932 | -10.4672 | -50.2838 | 2026-09-22 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| d006094e-e816-346d-9cd1-6dc21ab7c970 | -1.4487 | -48.9526 | 2026-09-22 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 45c4a4ad-a2fd-3774-a16d-c0be0ac9b14a | -3.7312 | -60.5828 | 2026-09-22 16:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| e23e4180-579f-3d64-9476-d01ba1026ca2 | -6.1111 | -57.6645 | 2026-09-22 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 166.8 |
| 37a029c9-91c3-3053-8253-e4b03d33fbb3 | -10.5748 | -46.7296 | 2026-09-22 16:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 332.7 |
| 3bd69a53-25ee-37a1-aa3e-0060287cee17 | -2.6966 | -57.5889 | 2026-09-22 16:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 95ee6dcc-e4e9-32e4-937d-bda8522567d5 | 1.3634 | -56.0834 | 2026-09-22 16:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| ffb125ac-5497-38ac-9ccd-56aaf8a2ab39 | -10.6726 | -50.4758 | 2026-09-22 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 94fcaf76-1322-31a5-a4a6-8da9afe62c83 | -6.64 | -59.9 | 2026-09-22 17:15:00 | MSG-03 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e16e134d-bc22-3eb8-9cd6-8d55e4a48ce9 | -14.72 | -45.6 | 2026-09-22 17:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6117f207-2b8c-382f-834a-a0f048750b19 | -6.64 | -59.98 | 2026-09-22 17:15:00 | MSG-03 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 61892f0f-df94-3b26-8bcd-999da16e2dfa | -14.73 | -45.65 | 2026-09-22 17:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8f841def-1bd5-353d-a983-124d4ab4615c | -9.61 | -43.94 | 2026-09-22 17:15:00 | MSG-03 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| aaae93fc-e496-32f4-9b48-dcf9d3551b0f | -6.61 | -59.97 | 2026-09-22 17:15:00 | MSG-03 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1e52afa3-2f49-3c3e-9dec-3fa8911c5eda | -10.55 | -43.96 | 2026-09-22 17:15:00 | MSG-03 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 30943269-38dd-39f6-981f-3f6d86c53eb7 | -5.9152 | -59.933 | 2026-09-22 17:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| d49ec1ae-135f-3562-8995-8fd87f2bb60c | -2.8608 | -57.7994 | 2026-09-22 17:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 175.0 |
| 97316efb-f638-36c6-bbcc-b2e82ec14a52 | -2.9326 | -58.3397 | 2026-09-22 17:30:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 89b3c311-91b3-332f-8ffc-fb863e2d4b2e | 1.2423 | -51.0178 | 2026-09-22 17:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 67.9 |
| dd71804e-413e-35d2-bb2a-35590dfadc58 | -3.8265 | -59.3215 | 2026-09-22 17:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 4ea72fa1-fe26-3dbe-869f-928e4afb5a1b | -2.9157 | -57.8177 | 2026-09-22 17:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| a69a91bb-a4a6-31e5-9c00-707858a19ff8 | -8.7706 | -45.8567 | 2026-09-22 17:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 94b22310-c0ab-3d16-8032-d61d50aea865 | 1.9976 | -50.8813 | 2026-09-22 17:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 58.0 |
| f1a83b1c-d718-30f8-a44c-dab86966e1bb | -3.6449 | -58.8647 | 2026-09-22 17:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| d0158859-61ab-3de5-9702-e48abce7882d | 1.9792 | -50.8817 | 2026-09-22 17:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 57.2 |
| e262a927-65f0-3120-a85b-6edd8dcebea7 | -10.7715 | -46.3001 | 2026-09-22 17:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 193.4 |
| b538e7a0-5b17-3037-96ba-b8e1250369bb | -3.2955 | -59.4476 | 2026-09-22 17:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 101.6 |
| d02b770d-cf7c-35b6-949e-bc383a258085 | 1.2607 | -51.0175 | 2026-09-22 17:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 5adde19f-1e5d-3657-8ceb-067f68824210 | -3.8264 | -59.3407 | 2026-09-22 17:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 0b31d941-4741-38da-bfee-a9d6e82f1cff | -3.6247 | -59.46 | 2026-09-22 17:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| f49165ee-6dec-31a8-93c0-ea3079af8c12 | -9.8404 | -46.3911 | 2026-09-22 17:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 248.4 |
| b93a0caf-f853-3a88-a0e0-675d3eaddaa8 | -6.8985 | -41.6976 | 2026-09-22 17:30:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 160.9 |
| f5ef1f7d-1493-321e-818c-1d93f8a5a8dc | -3.6066 | -59.403 | 2026-09-22 17:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 2610d2b1-d24a-38a5-ba9b-3a3fefa5bf96 | -2.9525 | -57.7394 | 2026-09-22 17:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 0ae41535-6aef-39c6-8a1c-9cbfb6c6ede9 | 1.1319 | -51.019 | 2026-09-22 17:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 9340145d-4418-311b-b6c7-d3129cae8a96 | -3.5757 | -64.43 | 2026-09-22 17:30:00 | GOES-19 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 28d8dbdc-b7fa-322c-bce4-b906420f5779 | 2.4396 | -50.9552 | 2026-09-22 17:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 58.6 |
| bc48cde5-5f54-39c6-9cfb-255f416c5402 | -2.8974 | -57.7987 | 2026-09-22 17:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 94.7 |
| daadc90f-9851-34d4-b69a-5dfea620d0f4 | 1.1318 | -51.0398 | 2026-09-22 17:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 3ca0f0ab-3aa4-33d3-b336-8451cac347b8 | -11.3784 | -44.2195 | 2026-09-22 17:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 255.6 |
| 26fc9d26-5e38-39dd-a935-333a8e947d72 | 1.9793 | -50.8609 | 2026-09-22 17:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 56.3 |
| c1ba3016-70a1-3a05-b651-3f6f5a5f2796 | -3.1851 | -59.6982 | 2026-09-22 17:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| e04fc046-0334-34a1-822b-23f4767d8a74 | -2.9528 | -57.623 | 2026-09-22 17:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| d54c3360-d761-325f-ae3c-7764d8e42093 | 1.2608 | -50.976 | 2026-09-22 17:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 81.0 |
| b1629983-44f5-3af5-95cf-152362030929 | -10.4475 | -50.3499 | 2026-09-22 17:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 1f50dc0d-2dae-3174-b73f-b0493f1bf6d9 | 1.1503 | -50.998 | 2026-09-22 17:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 54d8fb06-eaaa-39a9-acbd-e3645a969d8a | -9.7883 | -46.0593 | 2026-09-22 17:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 445cfb88-3b3a-30f3-8dbe-94ae062349c2 | -2.8974 | -57.8181 | 2026-09-22 17:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 03f6ba4b-8c40-36fc-9621-5607941e7f61 | 1.2608 | -50.9968 | 2026-09-22 17:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 79.1 |
| d3d89e0d-3bfe-3e75-9d9c-48f9d38d3641 | -3.7364 | -58.8626 | 2026-09-22 17:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| bd19d7b8-4755-3785-bdc5-a400010be66f | -2.9157 | -57.7983 | 2026-09-22 17:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 1732fde0-bda0-3032-876f-ea1dae5b895d | -2.5687 | -57.494 | 2026-09-22 17:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 7eb5ed41-d080-36ad-8ca9-d634531c3e36 | -3.331 | -59.8483 | 2026-09-22 17:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| c128356d-4435-3309-b3c5-b881b6b381a1 | -2.4206 | -58.2712 | 2026-09-22 17:30:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 129.8 |


[Clique aqui para ver as próximas entradas](README157.md)
