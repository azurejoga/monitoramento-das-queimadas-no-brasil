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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26d331e2-72d3-322b-8151-41ade053e71f | -12.48937 | -54.91732 | 2025-05-21 04:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb15021a-19c0-3ae1-8503-2becc04dff37 | -11.91855 | -54.40956 | 2025-05-21 04:42:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4c14f2e-3dad-3978-8dff-693949dbb7fb | -9.28615 | -57.55085 | 2025-05-21 04:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d80eb556-0b0f-3880-b1d8-fa08bf88136d | -14.16663 | -45.48283 | 2025-05-21 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db04f6f6-fed1-3c85-933f-fcb6bbe854ae | -12.72444 | -54.96934 | 2025-05-21 04:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 86678a0d-4d1f-3171-8ce2-31148b1844ec | -14.16401 | -45.47025 | 2025-05-21 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91a1351c-450e-3f41-9eb6-d196b8545dc6 | -13.67031 | -53.93545 | 2025-05-21 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f4794b9e-4c3e-305f-9de1-4431dffe0d83 | -11.29237 | -53.98086 | 2025-05-21 04:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c6dc4bba-0760-36bd-a0a1-e33e30432cc0 | -12.48644 | -57.19313 | 2025-05-21 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b983cc3c-76a5-3dd1-8a37-26462a673868 | -14.67188 | -45.10915 | 2025-05-21 04:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e14beb37-a463-30e6-b717-09b808dc174d | -11.57833 | -54.56566 | 2025-05-21 04:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9983340d-3295-33cf-857e-b5619ebffbdc | -10.90914 | -48.54256 | 2025-05-21 04:42:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7234231a-e3ff-3add-a940-a7c0ddc5076f | -12.34403 | -49.95961 | 2025-05-21 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b37796f2-def4-3a12-bc8e-7fadf750e32c | -10.64971 | -59.287 | 2025-05-21 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 24a18df6-ee08-31ec-a083-bf57c4daa4f3 | -11.08575 | -54.7772 | 2025-05-21 04:42:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 61413a67-0183-3d92-bbbd-0bb87d0717a0 | -13.51707 | -46.81605 | 2025-05-21 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d23c19c-ac1d-3f52-955f-bf77e0adcd05 | -15.04576 | -45.66343 | 2025-05-21 04:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32ec4292-5ea0-3179-a14a-cf9c7bd1505e | -11.20825 | -49.16683 | 2025-05-21 04:42:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4d0706d-9ed7-31dc-9c1a-daa574f854f3 | -11.23686 | -49.49864 | 2025-05-21 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5447fd75-4fc4-3842-81b4-bfaed9cf131d | -12.72285 | -54.97867 | 2025-05-21 04:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b59bbae-f29c-3ca7-a1b7-d448296d6bbc | -11.44965 | -54.09101 | 2025-05-21 04:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5d49a95-449f-31ba-bc09-e70586456dff | -9.94005 | -49.74435 | 2025-05-21 04:42:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b27eba6e-ecb6-3d5e-ac00-b731d8235b8f | -13.19581 | -47.27124 | 2025-05-21 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8579d038-170f-3fac-99e2-1bec83b85319 | -12.83431 | -47.39897 | 2025-05-21 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 957b4dbb-54df-34e6-abc6-68015b9ba634 | -13.79937 | -53.30124 | 2025-05-21 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dfb609f3-7126-3d34-9403-e2b69593c0fe | -13.66703 | -53.94023 | 2025-05-21 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7a0c3f6f-d000-3a03-91ac-bcb68ef7113c | -10.59856 | -52.8473 | 2025-05-21 04:42:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c12cbf8a-5edd-33c5-9f88-bf58bd6ca590 | -11.78515 | -44.28541 | 2025-05-21 04:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a6dc83d8-538d-3bb7-97fb-d32b5af1a919 | -12.87497 | -43.18172 | 2025-05-21 04:42:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 53450722-af75-307f-80a0-3e34efde2ed6 | -14.67625 | -45.10976 | 2025-05-21 04:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1272287d-d602-3a55-b432-e6e2c8d66e55 | -12.83867 | -47.39506 | 2025-05-21 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2785b515-7e26-34bc-8007-4f2659435e23 | -14.01818 | -55.1354 | 2025-05-21 04:42:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 639d7ca8-7ce7-3f44-995e-8cd27f70ac44 | -11.29969 | -53.9821 | 2025-05-21 04:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 37bca90f-396a-3dd1-a84e-eaf55a2fec39 | -15.26914 | -51.47176 | 2025-05-21 04:42:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbb3e851-9340-34f1-8752-3f0ced5bcaaa | -15.2697 | -51.46818 | 2025-05-21 04:42:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36510c6c-40fc-3b82-951b-ed82e4f2565b | -11.1537 | -48.68019 | 2025-05-21 04:42:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37aeaa49-61a3-3f1d-a88d-890c55ed5203 | -14.04094 | -50.51989 | 2025-05-21 04:42:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62a3e23e-3171-3ca4-baba-4a9c98eb1c68 | -12.29908 | -52.48335 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6e8d7748-684d-38e8-8040-bfb37d51e6f1 | -11.44231 | -54.08971 | 2025-05-21 04:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b4fd719-dac7-3647-ba89-4f8efc418d43 | -12.29166 | -52.48591 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d1dca86a-7a84-368e-9d86-c156dc3e01ca | -12.03577 | -54.96769 | 2025-05-21 04:42:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 873864a7-1263-32b0-a297-cc278e7b9aa9 | -12.34123 | -49.95549 | 2025-05-21 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f685b4ab-dc37-37c2-bf20-3bb4fb1319f7 | -19.73397 | -54.51117 | 2025-05-21 04:44:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e4c1780-5614-39e0-918f-b2281d1e287a | -19.11207 | -52.69275 | 2025-05-21 04:44:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e48051db-b9fb-3a40-b35a-793d73ea45e9 | -20.62432 | -55.03631 | 2025-05-21 04:44:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d797c7c-30db-3ff6-88d6-601f4ca3d37f | -20.47684 | -53.67379 | 2025-05-21 04:44:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d72dcc42-96d4-390f-b7fd-d6fcb754e99b | -21.12115 | -48.67354 | 2025-05-21 04:44:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 16f710e8-25e0-3f00-8cc5-40e9f4a7a47f | -19.05791 | -53.45669 | 2025-05-21 04:44:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7cbe2906-5d4e-34b1-a70f-21d7aa763d07 | -19.11366 | -52.70432 | 2025-05-21 04:44:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e099f0d4-c269-36dd-a3b1-df2480bd1460 | -19.1598 | -47.81908 | 2025-05-21 04:44:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f7588e7d-f9d3-3676-8d55-2bd818028ef4 | -17.15199 | -54.01241 | 2025-05-21 04:44:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| faceeee5-0ca1-3a46-9e49-7315bfdf633e | -22.54099 | -48.81356 | 2025-05-21 04:44:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d11f6bc8-f759-35e6-b0ce-20f5edb476e9 | -23.33909 | -46.77176 | 2025-05-21 04:44:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9df95f27-409f-38a8-a688-98bba64f75fb | -19.74148 | -54.50854 | 2025-05-21 04:44:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac70ac65-04b4-3965-a092-1189892c0484 | -17.91937 | -45.52528 | 2025-05-21 04:44:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6204886f-fe27-3296-954a-0e1fdde8320a | -17.70437 | -47.49827 | 2025-05-21 04:44:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bf7f00e-2eae-3d60-ad0d-e46fb5311760 | -19.06033 | -53.44177 | 2025-05-21 04:44:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55835a0c-7cb7-31fd-94df-1564d25a6918 | -21.45611 | -47.36536 | 2025-05-21 04:44:00 | NPP-375D | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 773e8a1c-6e0a-3205-b4cc-7967e65b2206 | -19.45329 | -45.30676 | 2025-05-21 04:44:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7fe6ca7-11d0-3c8b-85e7-28a98b462e3b | -15.48018 | -58.33593 | 2025-05-21 04:44:00 | NPP-375D | ARAPUTANGA | MATO GROSSO | Brasil | 5101258 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bcfda56-b6e6-3937-9200-3339cd42c1fd | -17.70828 | -47.49881 | 2025-05-21 04:44:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2df51623-f331-3091-b196-bcdcfee099da | -19.7449 | -54.50921 | 2025-05-21 04:44:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eff12e18-8897-3f2d-99c1-12a8c9f51489 | -21.0513 | -55.99754 | 2025-05-21 04:44:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86ab6a65-e182-3d69-8022-9b598fed39f5 | -17.75777 | -56.31191 | 2025-05-21 04:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| defaab1a-e206-357d-a96a-af01855c6336 | -19.33994 | -54.16863 | 2025-05-21 04:44:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 14565de0-5227-3dbc-9e9a-e99c0b06372f | -19.05907 | -53.45618 | 2025-05-21 04:44:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90bda078-5c57-3391-9f1d-e61a685030b4 | -23.70707 | -46.89449 | 2025-05-21 04:44:00 | NPP-375D | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6fbfd993-86ff-38d8-83fe-6ab9f8f93ab9 | -20.95526 | -56.59923 | 2025-05-21 04:44:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 46ecbae3-4a33-39d2-84ee-f2629c6bc37e | -15.27755 | -60.21248 | 2025-05-21 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 24fe0616-cbed-32d7-8c56-b986916df0be | -19.81213 | -54.41584 | 2025-05-21 04:44:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b90d1b1d-8a16-36e9-8687-3ea4a4883777 | -20.94994 | -56.60763 | 2025-05-21 04:44:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f0d0569-ea52-3306-b820-3dafd44c96a4 | -17.69482 | -54.09143 | 2025-05-21 04:44:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebfa5561-14a2-3704-bc7a-194db96184f2 | -19.11424 | -52.70066 | 2025-05-21 04:44:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad4206cb-a3d5-3ea3-976a-7da0f4efdb2c | -23.71148 | -46.89502 | 2025-05-21 04:44:00 | NPP-375D | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 293b4fbc-2b07-3317-8bdc-1e54630df7f6 | -20.99561 | -51.7909 | 2025-05-21 04:44:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f494e086-3e8c-3c51-997d-35188f25107b | -22.59999 | -54.9556 | 2025-05-21 04:44:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9ee0a611-0a33-3568-a30e-355ed07d52b3 | -20.73787 | -56.03431 | 2025-05-21 04:44:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ff344c98-455f-33c5-aeab-fecf279bece9 | -20.95444 | -56.60381 | 2025-05-21 04:44:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 939da3e2-09a5-3185-94b6-f31d0610db8f | -19.05968 | -53.45244 | 2025-05-21 04:44:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb88797f-98d5-37d4-89af-2fa049d4303b | -19.66309 | -51.3404 | 2025-05-21 04:44:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eea07cc9-ffd0-3c7b-a8df-ff56c08f816b | -22.31479 | -53.62907 | 2025-05-21 04:44:00 | NPP-375D | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ab8e2307-3b57-33b4-87f4-984c0866b243 | -17.91879 | -45.52987 | 2025-05-21 04:44:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21975276-b39d-3138-9d52-830880b46f0b | -20.76322 | -46.76905 | 2025-05-21 04:44:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 76c44197-9ec5-3a54-a999-fea82db5c87a | -18.29664 | -51.86079 | 2025-05-21 04:44:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 31111bb8-ab93-3878-b684-bae1926f5854 | -19.06152 | -53.44127 | 2025-05-21 04:44:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 579158a4-ea78-3cb4-a9b2-2b798185c707 | -20.22091 | -50.75386 | 2025-05-21 04:44:00 | NPP-375D | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 889c7635-c1a0-3109-8e24-a8590963937b | -19.70354 | -54.56599 | 2025-05-21 04:44:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4fc4839-d040-3246-9285-7a30aa4c63d7 | -17.5025 | -46.73828 | 2025-05-21 04:44:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4faec820-831f-3588-96a5-6278e096e1d2 | -18.87469 | -50.15497 | 2025-05-21 04:44:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 638ea57d-285c-3403-8495-c75a5c3cf63f | -19.05456 | -53.45609 | 2025-05-21 04:44:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f113e94c-3e40-3338-a927-e4337dc9fe89 | -20.95648 | -56.61365 | 2025-05-21 04:44:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96cd6d9d-d981-32df-bf4a-502de0507578 | -19.05852 | -53.45296 | 2025-05-21 04:44:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb4c1656-6a4c-319e-83ea-a053eeeba510 | -21.44212 | -57.12714 | 2025-05-21 04:44:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42646547-3f88-36a5-a3ef-977884b043da | -15.47778 | -58.33415 | 2025-05-21 04:44:00 | NPP-375D | ARAPUTANGA | MATO GROSSO | Brasil | 5101258 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b3f157f-b401-3a96-ae48-b6f394094eb0 | -19.82626 | -54.58413 | 2025-05-21 04:44:00 | NPP-375D | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9a40541-18c7-3e7b-af20-8a8ff00852a8 | -16.28418 | -58.67101 | 2025-05-21 04:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b6e82775-2454-31c5-950c-5cbebb24f861 | -16.28337 | -58.66842 | 2025-05-21 04:44:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4cd827b0-563d-3a3a-862f-a9d483acd7cc | -23.60617 | -48.28996 | 2025-05-21 04:44:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 10cb89d3-8ee5-326c-a9d4-4c305e23781a | -21.45976 | -47.37004 | 2025-05-21 04:44:00 | NPP-375D | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e2d6315-6a7a-3e1a-bc45-5d7951bae7f2 | -22.85786 | -47.61971 | 2025-05-21 04:44:00 | NPP-375D | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README15.md)
