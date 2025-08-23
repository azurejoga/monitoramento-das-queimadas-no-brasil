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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc705ae8-4114-35d9-b3c9-305f3ee36134 | -12.50649 | -53.81962 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9c6953c-6654-3b2e-a34d-0d7fa95fd4f7 | -11.19206 | -55.03532 | 2025-08-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0acad346-a829-3a31-a92a-dc0e781ee277 | -13.38477 | -56.61252 | 2025-08-23 04:53:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92fa8877-5803-3ea8-b457-6f8fdb84baf2 | -14.35297 | -53.12133 | 2025-08-23 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2a9f35a-2fff-3f26-a248-56e8e7ee9b17 | -14.77631 | -45.23149 | 2025-08-23 04:53:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30015286-4eb5-38cd-ad2c-9b6a071d7033 | -13.13775 | -57.1201 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cb59073-a1df-3feb-b30b-e5a634adfd0e | -14.86178 | -59.61337 | 2025-08-23 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b9d8e87-64b3-3ab0-9851-970329a1c7f6 | -12.9966 | -45.22919 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4ee877c2-cbc4-3065-9652-8ff2d6a67d63 | -12.30212 | -50.00586 | 2025-08-23 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48964819-f200-38f9-acc7-dd116fe32141 | -15.56098 | -42.68233 | 2025-08-23 04:53:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 35b99485-c220-3925-91fa-598e61f343ca | -9.84702 | -64.28921 | 2025-08-23 04:53:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be3e8360-473f-356d-a13a-090b97d2ce13 | -14.75519 | -55.99057 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f7507fd-8535-342a-b1a6-a9d734fd3fb7 | -9.95938 | -60.18855 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| c39d0e24-aed7-3094-a544-c7b3ebc08b58 | -14.47407 | -56.4852 | 2025-08-23 04:53:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 228d5569-75af-3c05-9476-328aeb24d1fb | -11.97307 | -46.77145 | 2025-08-23 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1287bd82-0bfd-325d-a914-dded53697983 | -15.07462 | -48.49671 | 2025-08-23 04:53:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71c098d4-3dd4-3125-ab13-c0ff5e5655e3 | -15.54817 | -51.70541 | 2025-08-23 04:53:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| deb21eb2-b29c-36e5-bfbc-4d608a6f2c26 | -13.04244 | -46.33032 | 2025-08-23 04:53:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 17329a2b-77a2-3aa6-af0a-36df578bb746 | -17.26749 | -46.76743 | 2025-08-23 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f5398749-e0b6-358d-bac2-bd3d58c84555 | -15.65421 | -52.68117 | 2025-08-23 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f9ee321-f093-3259-a82e-f32eb69105cd | -14.68204 | -56.61001 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8da2e89c-a6a2-3eaf-af80-191216e84664 | -13.0268 | -56.87462 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8475f546-f9d7-3e1d-9012-6b15128664f9 | -9.51222 | -60.5178 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ebbcfab-e1ab-3298-9708-5733408dbbe8 | -14.66552 | -54.91199 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2ba6dbe-21f7-3622-a967-6a5253efd5c5 | -11.19714 | -55.02509 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 050e3f21-e61b-399f-8888-dd83d9c768ff | -10.46203 | -59.13779 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21a4fab6-e42a-3ede-ba1b-b50af350a3d8 | -14.47622 | -46.05874 | 2025-08-23 04:53:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9c05bd0-3751-342f-a028-6927714e7290 | -14.82106 | -47.95218 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 25919013-e159-3bcb-9ed6-74f1c19b3220 | -9.95741 | -60.18073 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 951e1bdd-d500-36d9-85d1-922c0c9ab0ea | -10.4088 | -57.67821 | 2025-08-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d796265d-fb97-3140-a6da-db656d8801ff | -14.65085 | -54.91709 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80dc31d8-261b-35a3-aeed-b4810bc7c74f | -12.58712 | -60.34911 | 2025-08-23 04:53:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7da79743-2690-3b12-9063-6608bf9fcb27 | -17.26684 | -46.77337 | 2025-08-23 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 931ba26c-cfed-381f-bf9e-baac88098e7f | -13.49903 | -47.03977 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09d96a27-7935-3441-aa7b-f0bb917862b6 | -8.89075 | -62.43555 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7da243b4-532a-3c93-9123-8ab74ea1bfdc | -14.64706 | -54.87639 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a1c779c-a0e5-3c78-be98-51e387a09f16 | -13.02701 | -56.82253 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8ed60b04-f18e-3a8f-bbf4-643dfcda21bd | -8.88141 | -62.42712 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd3e9803-a139-35a6-8426-f23c1c0f2612 | -13.03683 | -56.82832 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2caad47-4769-314d-a487-63f0261ff1ce | -12.99134 | -45.22846 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| cceec21f-b3b3-3ca4-a344-871df02374d0 | -11.27268 | -54.20623 | 2025-08-23 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb075a2e-7655-3832-bb95-569fa50c150d | -14.28782 | -58.52674 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7be42ddc-7ac8-3099-aa07-7cd1624807d8 | -14.65191 | -56.60123 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ce78b25-372d-3994-bcaa-be58c29e2fa6 | -13.02441 | -56.83834 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2b1dfba-7875-358f-b078-c6b44a4c0a17 | -14.96621 | -48.67382 | 2025-08-23 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b43ee0df-e50b-3dc5-8bad-b39429ed79ce | -13.46241 | -47.0282 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| dd65aa25-997f-3370-ba04-329739345f1b | -14.38045 | -52.05916 | 2025-08-23 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb60b112-56d7-33d7-bb3e-1f4892fed5a8 | -9.95495 | -60.18774 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 6bd59810-fcf9-38c8-8f06-aa6046a8a3ed | -14.78606 | -45.48223 | 2025-08-23 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 80003471-db42-3959-9370-4601b4f7c945 | -15.56272 | -42.68695 | 2025-08-23 04:53:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 30c43223-dc7e-3311-a91f-5cdaad3bef3a | -14.75459 | -55.99424 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93b83928-7c5a-3fe6-9f3d-b68cae416983 | -14.73522 | -56.02864 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 824f3e88-987c-3f19-a1a9-a2f288aa9dc0 | -17.2727 | -46.76803 | 2025-08-23 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa1377a8-3ece-35d9-8639-99cdf375a269 | -14.26676 | -58.53702 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a8f7bdf-c828-391c-939b-03a72cc7e6aa | -13.00225 | -45.2266 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e4d39a0d-e8a2-374c-bef8-bb60494e3423 | -14.79718 | -45.43205 | 2025-08-23 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c0cf827-f03e-3009-9215-67848548b287 | -14.46844 | -55.93445 | 2025-08-23 04:53:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c18e660f-e5a0-3e6e-84c4-eeca406a9996 | -13.0451 | -46.3254 | 2025-08-23 04:53:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49ffe840-9807-31ef-94fb-f7bf53c7fe5e | -15.06914 | -56.38979 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d70dbbb1-c343-3cfc-ada8-b6bff62d1fb7 | -14.67647 | -56.60118 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b79ee76e-c166-39cc-9187-861ac9071400 | -13.38245 | -46.21366 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fa578efb-f29f-3358-b13a-fd13edf09667 | -8.89726 | -62.42731 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0bdcbfdd-031f-3721-a606-8bd720cdcd85 | -14.57894 | -54.508 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65cf3b03-44d5-3e65-9554-19ba5f537676 | -14.51606 | -53.04379 | 2025-08-23 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3480399-ec9d-3716-8739-09acbd46deb5 | -14.54747 | -53.24987 | 2025-08-23 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9750c76-b408-3dc2-9eb5-38f54519f26e | -14.60148 | -54.77781 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6173376d-44de-3c0a-8d5a-80877b806354 | -15.02244 | -54.8692 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14d8751b-124b-3626-a21b-e891f6147507 | -9.50849 | -60.51223 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3627631b-336d-3f08-915e-d26348f3bfe0 | -9.46616 | -60.37607 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ae4cf888-2bac-32d9-a0ad-05870d0b8703 | -14.62508 | -54.84359 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a77b2791-10f0-3fae-b214-2a6bc6da8533 | -14.97049 | -48.67446 | 2025-08-23 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38e5b099-6abe-336b-a55e-b0c93ad52a79 | -10.61174 | -55.40715 | 2025-08-23 04:53:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bd8695d-07e9-3706-8e8f-45f3140850b2 | -15.82989 | -56.10173 | 2025-08-23 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6395d101-e80c-3daf-8dd0-dcf9710c203c | -13.03327 | -46.324 | 2025-08-23 04:53:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 759f725c-fae8-3ca0-900c-5fbc101b9845 | -9.21765 | -60.7903 | 2025-08-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 810f512e-1459-38d5-9913-ccb8d751a450 | -14.37811 | -52.05062 | 2025-08-23 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0a3d190d-ec0f-3309-b6db-bd4b528f9259 | -13.6882 | -57.75415 | 2025-08-23 04:53:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 65ce3126-8cd6-3849-ab85-7b5c0cebf26a | -9.9493 | -60.17474 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e3bd7be3-e466-31c9-bc02-6b783f2cb495 | -14.62014 | -54.83185 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afed0032-2ca6-38bb-b8dc-1cdcd4611be3 | -14.92293 | -47.32313 | 2025-08-23 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8e78ef7f-0f18-3874-8f23-8521b4eee0fe | -9.5139 | -60.5083 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9df44faf-971f-361a-ac00-198c8390a9f9 | -14.61412 | -54.80537 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 960fe820-9c62-34a2-9152-6773943ff274 | -14.94405 | -55.99955 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bed623d1-35d9-3681-ba70-60595a694c80 | -14.66827 | -54.9161 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d45f25e1-90e4-3928-b35b-6c2a7655ae0b | -8.89718 | -62.42995 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef78e484-8f25-322d-a543-3ef65d7dc385 | -8.8855 | -62.43459 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e351072-0d1f-38f0-8832-f407e3481734 | -14.65659 | -56.59413 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a24250d9-c3bb-35b1-863d-f0c94583326c | -14.57344 | -54.49982 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b9f2ae5-8c26-38f3-899f-2acbd79d0ef8 | -10.46657 | -59.13007 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 247f0f79-5064-30a8-bf24-5467fca46fd7 | -15.01858 | -54.87222 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d34df71f-390f-362c-a905-c9772f5ad286 | -14.36702 | -52.05301 | 2025-08-23 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddbbe98c-ab5a-369f-b76a-8d05aa512e31 | -8.90191 | -62.43151 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ae506beb-1f16-32ff-8f0e-f4800cc295e4 | -13.03764 | -56.83165 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a4a5d4e-71be-3b48-bc1a-4f90a84a2c8d | -11.1871 | -55.02346 | 2025-08-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96901555-d842-3a6c-b5d3-3cf37f4ebfdd | -13.04085 | -46.31981 | 2025-08-23 04:53:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 264e990e-4caf-3a79-aabe-5787ac5af005 | -10.60776 | -55.41026 | 2025-08-23 04:53:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71af92e8-8ae1-35e0-bd4d-073dfa5004bc | -13.03399 | -56.82376 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b127cc28-ce0b-340e-9c1e-bccf1dfadc77 | -13.50372 | -47.04038 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6de4f82d-8634-3111-8dad-7e0ca9c56892 | -8.9013 | -62.43479 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 92fb1b25-2f1c-305a-bc97-abba56fc7174 | -9.95574 | -60.18335 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |


[Clique aqui para ver as próximas entradas](README50.md)
