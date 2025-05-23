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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 043d5efa-2a53-3573-b617-70307b579ba0 | -9.0241 | -47.748798 | 2025-05-23 00:57:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c0e268ce-dd26-3c00-8d50-53d81127ef2f | -12.4168 | -49.985802 | 2025-05-23 00:57:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d8117db4-40cb-30d8-acef-d6148e4befaa | -6.2299 | -43.400398 | 2025-05-23 00:57:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0919b052-2d92-311e-a147-391960173973 | -12.3253 | -49.9921 | 2025-05-23 00:57:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b42929a7-f771-3a17-bce2-8a8f3237a7ce | -12.3955 | -49.983101 | 2025-05-23 00:57:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ad627b74-489f-3766-a4d0-725577392dc7 | -10.8216 | -56.953899 | 2025-05-23 00:57:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4cb6832-8544-3903-a894-93a128aa19bb | -10.7211 | -48.836899 | 2025-05-23 00:57:00 | METOP-C | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5bfbdd7e-ff73-3990-a915-d56c6d56bb17 | -13.1509 | -56.820499 | 2025-05-23 00:57:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1fb17015-8d30-365a-8907-c09efc975fa1 | -11.3004 | -53.987499 | 2025-05-23 00:57:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26cdbe1b-a5ce-37d6-9ec8-339acca39253 | -12.3334 | -49.982498 | 2025-05-23 00:57:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f8658baf-fc71-3c9a-8a72-9cd214e6b359 | -11.5124 | -48.557899 | 2025-05-23 00:57:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f7b029d3-040d-373a-ab7f-111981f41c53 | -7.2241 | -43.150101 | 2025-05-23 00:57:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 075e7b53-ce67-3dd1-8686-dce4e4d2d591 | -10.6558 | -49.477501 | 2025-05-23 00:57:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bbbf88f2-886e-3e0d-b0fd-8ef891884240 | -10.3669 | -57.509602 | 2025-05-23 00:57:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb09678a-9b5f-36d0-ac42-60cc8fbdf4ba | -11.5144 | -48.566299 | 2025-05-23 00:57:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 705954dd-50d2-348f-b119-9a673c0505f6 | -14.0267 | -55.132702 | 2025-05-23 00:57:00 | METOP-C | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7eca7de4-12ff-3a1b-91b7-2acfed125443 | -9.9716 | -49.818298 | 2025-05-23 00:57:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e23b2eee-e6b7-36be-a87e-3188ab0bb38f | -23.1234 | -47.499401 | 2025-05-23 00:57:00 | METOP-C | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bfeb2cde-84ed-3f54-948d-8d98fb99f6ae | -14.0548 | -53.384399 | 2025-05-23 00:57:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d540fd24-e51a-3c72-944a-1fd91c3b1bfa | -9.96 | -49.813 | 2025-05-23 00:57:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f95c78fe-db1d-3dad-8be0-921b11b6f898 | -13.7836 | -54.319698 | 2025-05-23 00:57:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0e11e752-ef27-3e3b-9101-c91c37a4fab3 | -13.9823 | -56.001801 | 2025-05-23 00:57:00 | METOP-C | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 83f9eba0-b05e-3fe0-8f9b-917f86903f14 | -11.7849 | -44.299599 | 2025-05-23 00:57:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b02a6f11-a553-38a8-9778-b25e7acae7b7 | -11.2906 | -53.989601 | 2025-05-23 00:57:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2ad57087-2387-301e-b037-79e9ea61d2dc | -13.1533 | -56.831799 | 2025-05-23 00:57:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f98dbd5-55ed-3700-8cf9-7d569c160abc | -10.8119 | -56.956001 | 2025-05-23 00:57:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c2994f68-4adb-32e4-833d-ca2c474028f6 | -12.327 | -49.999401 | 2025-05-23 00:57:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a964cb2-74a7-3f46-93ee-6c6b913dc2c4 | -10.6576 | -49.485199 | 2025-05-23 00:57:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3d09b46-47a3-37e5-8df5-40b8bc5c36cc | -12.0813 | -47.356499 | 2025-05-23 00:57:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 20ab4a05-f746-3766-9d38-746ef88619be | -11.3087 | -54.0257 | 2025-05-23 00:57:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9056dfd2-814f-3151-9737-1f60dd8ffb36 | -12.067 | -47.34 | 2025-05-23 00:57:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a9103f2b-50d0-3f8f-8128-b2b7c8bccb26 | -12.3173 | -50.001701 | 2025-05-23 00:57:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1d05759c-5b9e-3fad-9259-e8fe8f0289f5 | -12.0693 | -47.349499 | 2025-05-23 00:57:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cbec1803-0d6f-34a1-b5a7-e378f3cc00b1 | -9.0265 | -47.758598 | 2025-05-23 00:57:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e955f49-acac-343c-b1fe-73d4f8c9404e | -13.9746 | -56.014301 | 2025-05-23 00:57:00 | METOP-C | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4d92550a-4acc-3843-a6f5-bf78f7f60080 | -11.5598 | -47.465698 | 2025-05-23 00:57:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c2b5e00-e0c9-3aeb-b62a-7dafbcf873a3 | -7.2145 | -43.152599 | 2025-05-23 00:57:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4746b33a-06c2-3c03-b30e-b83dd29f812b | -11.7908 | -44.2822 | 2025-05-23 00:57:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 900c09dd-a8a3-388b-889c-1a5aa68d3bff | -10.6478 | -49.487499 | 2025-05-23 00:57:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0bfe9b8a-cb88-3efc-a086-3eacd92264cd | -12.8478 | -47.4035 | 2025-05-23 00:57:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0299548b-449b-3a0e-aa03-577e61cf4205 | -10.7093 | -48.831001 | 2025-05-23 00:57:00 | METOP-C | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8974470c-cab5-3664-b9a9-1c5da1dac473 | -5.5828 | -45.221401 | 2025-05-23 00:57:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4438ac4-1a58-3edd-9d4d-299217a5a1e2 | -9.0436 | -47.744099 | 2025-05-23 00:57:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70a829e8-2c56-3370-b786-b17eec63f139 | -13.0956 | -52.291199 | 2025-05-23 00:57:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b807f1f-a36a-3f4f-a424-87f74f53dc31 | -12.4185 | -49.993099 | 2025-05-23 00:57:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3fb8504-937a-30f0-a0a0-43ee70a32f82 | -9.046 | -47.753899 | 2025-05-23 00:57:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 66058904-91a1-3d62-b3d7-a7945746416c | -11.5713 | -54.570499 | 2025-05-23 00:57:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8e5d82d9-1516-3a68-9125-96b0d33bfd5d | -7.7113 | -45.671101 | 2025-05-23 00:57:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c8138b1-211a-3766-8a85-3bcf13e59a7e | -12.3368 | -49.997101 | 2025-05-23 00:57:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35258b9c-16d5-3dc3-994e-41c4c9bd1b12 | -15.2621 | -51.479401 | 2025-05-23 00:57:00 | METOP-C | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ac057f33-218c-3670-8b2c-be160696ece5 | -6.229 | -43.355701 | 2025-05-23 00:57:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bbd2f85c-950a-3dcf-9a69-a1ac83bc0fb0 | -11.8056 | -57.365002 | 2025-05-23 00:57:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d9dfedd-f46a-3bc7-b45f-1f7fc2b02d65 | -14.0287 | -55.141998 | 2025-05-23 00:57:00 | METOP-C | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 968e0f64-adf8-3108-90dd-ecf82577fb7b | -20.853701 | -53.763199 | 2025-05-23 00:57:00 | METOP-C | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8ec9c7e8-3cdb-3046-a7d0-42895eac6f4d | -19.7889 | -53.842602 | 2025-05-23 00:57:00 | METOP-C | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6fda2e10-3852-37e7-83c4-417cb59032c9 | -11.8031 | -57.353298 | 2025-05-23 00:57:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b701101b-903f-3d54-be01-64b7748aaced | -23.125099 | -47.507099 | 2025-05-23 00:57:00 | METOP-C | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a0016fb6-b851-3c6b-bbbf-427e5c973d13 | -9.0483 | -47.763699 | 2025-05-23 00:57:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 598d2db0-2eda-320b-b460-971e486d3417 | -20.849899 | -53.743698 | 2025-05-23 00:57:00 | METOP-C | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e9b80a7d-cc12-3de7-9002-de217f7fb9fa | -13.7819 | -54.311401 | 2025-05-23 00:57:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2f32d208-f82b-3777-89cd-aea0f6cd18ef | -11.5575 | -47.456299 | 2025-05-23 00:57:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e4732f4a-a43f-3b1e-a7fe-3348b5a276e8 | -20.851801 | -53.753399 | 2025-05-23 00:57:00 | METOP-C | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4cf18a84-5bd3-31f3-9ab6-b355591117a3 | -13.9767 | -56.0247 | 2025-05-23 00:57:00 | METOP-C | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a4823554-72ef-3b72-8fb6-a40b0e9caf2b | -11.7984 | -44.311901 | 2025-05-23 00:57:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bd880659-bfc3-3242-8bc0-7ccfc2940bf2 | -14.0531 | -53.376598 | 2025-05-23 00:57:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 736f53d6-bfbf-3935-91df-d00d43049be5 | -14.0434 | -53.378799 | 2025-05-23 00:57:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7777a9b6-d752-3131-998d-6611e5f98737 | -12.3324 | -49.9857 | 2025-05-23 01:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| c60d702f-ce6f-359c-b1c7-96028b0b485b | -14.001 | -56.0131 | 2025-05-23 01:00:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| e33d521d-8b81-3851-b57b-c6612d433ce6 | -11.7796 | -44.2762 | 2025-05-23 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 2ec6108b-20e9-30ec-ad37-42480be0c4ec | -7.0695 | -44.9335 | 2025-05-23 01:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 4abbc684-0d2b-376c-b241-2f20cbb81b8c | -5.5876 | -45.2091 | 2025-05-23 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 26ee29ce-5ee5-31b0-9932-5d03c0a068cc | -13.9818 | -56.0151 | 2025-05-23 01:00:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| be94df85-fe49-35d8-82bf-dc2d7d97540c | -11.7988 | -44.2733 | 2025-05-23 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| f831f657-8c4b-345a-89d5-7bb3bafdfb05 | -11.7988 | -44.2733 | 2025-05-23 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 93befda8-a4d6-3b2c-8a33-45f4ade42ec8 | -14.001 | -56.0131 | 2025-05-23 01:10:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| e7d97efe-010c-3ea2-8f44-4801d32decd8 | -13.9818 | -56.0151 | 2025-05-23 01:10:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| adf8ec98-3851-31f5-98d1-fed295fb4dfa | -7.0695 | -44.9335 | 2025-05-23 01:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 7620ad44-544d-3a50-a7dd-f99116e907ad | -9.0291 | -47.7452 | 2025-05-23 01:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 3ef03a1e-4274-3620-9824-560c67c9d7eb | -13.9818 | -56.0151 | 2025-05-23 01:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 63299e41-4961-3d0f-a6b0-751c0fe8312f | -12.3324 | -49.9857 | 2025-05-23 01:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| f8bdb711-f481-3dc1-9bc8-6a339d42461a | -7.0695 | -44.9335 | 2025-05-23 01:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 3880e2a7-44d7-3263-8ece-080495c26d4d | -14.001 | -56.0131 | 2025-05-23 01:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 41.2 |
| d8d28a34-1396-38f2-8059-cd874a7b5701 | -13.9821 | -55.9947 | 2025-05-23 01:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 48.9 |
| d074a223-b5f1-39ab-a26c-dd3d7ea0514f | -12.3324 | -49.9857 | 2025-05-23 01:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| ff659c00-bcec-3e62-bc59-e3d738835992 | -9.4188 | -40.3944 | 2025-05-23 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 69.5 |
| 85cd0156-5c89-3e84-a14f-616dab119607 | -9.4192 | -40.3695 | 2025-05-23 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 76.4 |
| d4e1b35f-b765-3d2d-a46a-cb2acfed198f | -7.0695 | -44.9335 | 2025-05-23 01:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| d503b776-d5a9-347b-b278-400f0d82b003 | -13.9818 | -56.0151 | 2025-05-23 01:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 3d1b1a75-486e-3ad2-8dc8-04f8e640d6e5 | -9.4383 | -40.3668 | 2025-05-23 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 71.5 |
| 6079952c-a449-3cde-8c6c-cf51d2e4c43d | -13.9821 | -55.9947 | 2025-05-23 01:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 338df343-37b2-37e1-a785-2585fdd10149 | -9.4379 | -40.3917 | 2025-05-23 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.0 |
| 36777850-f3a3-313b-a485-e3830ab5dec6 | -21.7206 | -55.3638 | 2025-05-23 01:40:00 | GOES-19 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 57.4 |
| b701eae5-6b5b-3658-98ed-80a2bff48214 | -9.4188 | -40.3944 | 2025-05-23 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.7 |
| fc50ebb3-15ed-3c14-bfc7-33d35b910823 | -7.0695 | -44.9335 | 2025-05-23 01:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| da5118e6-ac19-3bf5-9b0c-503319a60184 | -13.9818 | -56.0151 | 2025-05-23 01:40:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| ee314e47-5399-371e-a1b2-9cf6a69333b1 | -9.4379 | -40.3917 | 2025-05-23 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 90.2 |
| 52c088ed-6174-329a-a561-196485c9836b | -9.4192 | -40.3695 | 2025-05-23 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 61.7 |
| a1bf0e8a-756b-3dd0-8cc7-44beef82b40c | -14.001 | -56.0131 | 2025-05-23 01:40:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 42.9 |
| ac65ab29-ea2b-30e5-87f2-612009b4c17a | -9.4383 | -40.3668 | 2025-05-23 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 82.0 |
| 58434150-2f26-3867-a737-62350905a7fe | -13.9821 | -55.9947 | 2025-05-23 01:50:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 42.8 |


[Clique aqui para ver as próximas entradas](README5.md)
