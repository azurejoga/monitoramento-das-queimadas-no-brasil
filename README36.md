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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cabce5ab-2055-3efd-8f29-7c021c396ebd | -7.1072 | -42.0412 | 2025-10-16 03:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3e29ba3c-9fdc-3991-a032-064815d94e84 | -7.21765 | -45.16873 | 2025-10-16 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63eb0c00-a896-34b4-a883-872cb1f53676 | -14.7698 | -41.62286 | 2025-10-16 03:49:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fc14e634-9e24-3d2c-af67-8ed8b9139432 | -7.10619 | -42.04109 | 2025-10-16 03:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9b30fddf-795a-3b97-9284-5d37eecd8bcc | -7.27883 | -41.96114 | 2025-10-16 03:49:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 157a3ced-b542-3c69-8803-faa4bf72a0ca | -7.75556 | -42.47572 | 2025-10-16 03:49:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1d6a37d1-e6f0-3be3-84df-9fbc5931a5d1 | -7.55487 | -43.9178 | 2025-10-16 03:49:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70f80393-619b-39b2-b68a-4b72eb9c4ee0 | -7.05806 | -45.05544 | 2025-10-16 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 16ff52bd-5899-31db-8208-03af883a8d79 | -8.18505 | -43.32056 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 3ec33b2b-a7bf-34c4-b6a6-8577438d7fbf | -15.9638 | -43.01846 | 2025-10-16 03:49:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14d3ed54-6731-347f-bc5d-02134d2cb0b3 | -7.27812 | -42.94843 | 2025-10-16 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 90b15183-1644-3267-bc12-8e108ca38e56 | -8.27083 | -45.91584 | 2025-10-16 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28e6000f-8c37-36fb-81b1-e4453af74a31 | -14.63724 | -42.3966 | 2025-10-16 03:49:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 25fb6539-7fd5-3a16-8d6f-0bdb86260fc9 | -6.82892 | -42.7708 | 2025-10-16 03:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ccfdd721-119b-3c9c-9fdd-7c706ace03a2 | -7.29916 | -41.96463 | 2025-10-16 03:49:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ba76433f-64e7-30bf-ba4b-414ab6d902a6 | -7.48638 | -47.03149 | 2025-10-16 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82eb7434-27ae-38a7-82a7-9e4607d86d31 | -13.67358 | -44.28443 | 2025-10-16 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bbd9ec7-0654-391a-b11e-5be65a7364dc | -7.30913 | -41.85585 | 2025-10-16 03:49:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 51dcf162-d441-3a6e-a8b0-711ea34ab486 | -7.67734 | -42.5543 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5428a76c-5d46-3ac7-b676-28c903098ac6 | -6.17606 | -46.74236 | 2025-10-16 03:49:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 242e3570-0b26-3448-96b4-b3d448ef637d | -18.21442 | -46.06157 | 2025-10-16 03:49:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44be1dad-0975-327e-9c49-adaf7f1da0b3 | -8.45034 | -44.18915 | 2025-10-16 03:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a865f2b0-dcea-3ad0-85ce-6ede82711245 | -7.53423 | -44.28082 | 2025-10-16 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c68d60b8-0939-3735-8e82-76751794f3da | -15.02495 | -47.31448 | 2025-10-16 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94ae8322-a050-3d89-becc-a960f70844e5 | -7.37039 | -44.68411 | 2025-10-16 03:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6383a34e-c546-3d1a-ab10-f9a2e5afd9c3 | -7.94568 | -44.14388 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| c47d54f3-2f95-3330-97ff-37fa16503b2c | -7.94819 | -44.12922 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ada98bf4-e958-316a-a963-dd250f9e55e8 | -8.17113 | -34.98035 | 2025-10-16 03:49:00 | NOAA-20 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 81298e47-249b-3b57-8541-2422718f0af0 | -7.05754 | -45.05835 | 2025-10-16 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a548fea3-4511-3237-a1ec-d676e253e556 | -7.54019 | -42.06898 | 2025-10-16 03:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b3595a7a-e3b8-3b6d-b8d4-2a51273e08f8 | -8.18868 | -43.3256 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 6a28b184-4538-39e4-ad54-d786eac26259 | -14.64712 | -42.38401 | 2025-10-16 03:49:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9ac61cc8-d5d4-3b06-8173-73cbc4a91a2c | -14.11399 | -42.67611 | 2025-10-16 03:49:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 106041be-2e7e-3c71-b2fe-dde758d25702 | -7.55617 | -43.91731 | 2025-10-16 03:49:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4add2910-e53a-3393-8f08-979711664ed1 | -7.31107 | -45.75726 | 2025-10-16 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e00752a-4782-35b1-9fd2-e9a4e9e2142e | -7.25652 | -41.74466 | 2025-10-16 03:49:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 31.5 |
| 0e4c74d3-2a02-3791-b7f2-5a7cbf62878f | -13.65195 | -43.92208 | 2025-10-16 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0e20147-f969-3ea9-adc7-d20b2a0941ec | -7.30581 | -45.75634 | 2025-10-16 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3122298-0e93-3d33-aa1d-a8b19c819cbe | -15.58151 | -42.38223 | 2025-10-16 03:49:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df9e4070-042a-308e-bf1f-7c879aa38ef4 | -8.19693 | -47.01659 | 2025-10-16 03:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 54ec51d3-1087-38f4-b330-0d02417e3759 | -15.38438 | -39.21749 | 2025-10-16 03:49:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0d5f1aff-1aac-3399-bda6-bb0a5738463c | -7.4831 | -42.75042 | 2025-10-16 03:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3c7f4fd9-a1ab-384c-af15-28dd63756bca | -7.94354 | -44.12833 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06c665c9-75db-387c-9d44-cd38128ee7d6 | -6.4552 | -44.5839 | 2025-10-16 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff49324c-5712-3976-9136-b66a69e64893 | -7.03674 | -41.81163 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b2bc2c4b-21b8-3e4d-9710-98b6a2c409a1 | -8.29245 | -43.40628 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 08a6e52d-5f2b-3d73-826f-d82e25ad9653 | -7.47317 | -42.75704 | 2025-10-16 03:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 18a8df27-da87-3751-8ee4-46a4a42987df | -7.92874 | -44.13071 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 167ca2ae-5dca-37ce-801c-b6d211c5272a | -13.47578 | -43.60114 | 2025-10-16 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cc72c4e-fbec-350b-8837-4c88cd27faa1 | -12.23256 | -49.39362 | 2025-10-16 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09166ad2-8aaf-3f46-955f-f0d9931c5264 | -13.43467 | -43.62503 | 2025-10-16 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c86ac9a8-97c3-3ea8-a9c0-0674be37648a | -15.78217 | -43.65691 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8aa7a19-d6e5-3d96-a0c4-8533a060bfa3 | -13.11444 | -43.68713 | 2025-10-16 03:49:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3dc4e294-8157-3b6b-a794-213373d1103e | -7.60861 | -46.48096 | 2025-10-16 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f7a8999-f357-3687-9366-4f03063d3e8b | -7.62616 | -44.08524 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7949aa45-185e-375c-8750-76f4a5a76a1c | -16.2439 | -39.49302 | 2025-10-16 03:49:00 | NOAA-20 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| db936859-49ab-31df-9d52-c3185d9d8ffd | -8.07269 | -45.42825 | 2025-10-16 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76996e54-c923-3987-965f-23458ac9dccd | -7.53658 | -42.06829 | 2025-10-16 03:49:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2c53e9d6-22c6-3568-9617-3a4e1f33cd20 | -7.96438 | -44.13421 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e2d0b75c-eadc-3f16-99cf-f06cb008868d | -8.06752 | -45.42788 | 2025-10-16 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 795b69db-7f25-352a-98b5-0e6e8fd9a712 | -7.38838 | -44.75466 | 2025-10-16 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 800c476a-4360-362d-bc9e-28208dd246c3 | -7.27304 | -42.95187 | 2025-10-16 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 771411f7-a819-33e0-9b55-b7befb90c22a | -12.2386 | -49.39504 | 2025-10-16 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9c36125-1b41-3040-b4d1-9e369fff2aa1 | -8.25299 | -43.34574 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9fafad96-cd66-376d-adb6-dd709060fcb8 | -7.10682 | -42.03744 | 2025-10-16 03:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e5be7ac4-41fe-3136-93a6-5a0c5d5fc5bb | -7.94652 | -44.13897 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 02da1bda-8213-3668-822f-e2af653d5010 | -7.67178 | -42.56137 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c5e5a869-6886-326c-b326-c1e58906b67c | -7.07417 | -45.45189 | 2025-10-16 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e022d37f-9d9e-3425-bcf9-7b4c1766eadd | -7.24153 | -49.52011 | 2025-10-16 03:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4bb399a5-cca4-3fe1-9b66-db158db96956 | -8.229 | -44.02521 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e93430f-2282-3301-a323-cec13cb73a66 | -7.2963 | -41.95674 | 2025-10-16 03:49:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8f8c4868-0cce-381c-b56d-27792687e28d | -8.2457 | -44.03814 | 2025-10-16 03:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91317783-d1d0-3d11-ae67-ff0d79030d47 | -7.00546 | -43.74929 | 2025-10-16 03:49:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 406d23bf-fc69-3d51-8a41-3fe4b01ab2d7 | -7.57615 | -42.68663 | 2025-10-16 03:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f4d0e5d9-a860-3cf7-956b-b59038a342ac | -7.11192 | -42.03818 | 2025-10-16 03:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3715f18a-97a3-3183-95db-1a30786ff70b | -16.66617 | -42.11191 | 2025-10-16 03:49:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4407933a-c141-33c1-ae70-a28b438ebaef | -8.06808 | -45.42481 | 2025-10-16 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 243c69ba-80af-3a29-b494-00c248ffb9de | -7.35336 | -43.85818 | 2025-10-16 03:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 0c57c812-b84a-3b99-ad5d-132ef4e54b19 | -16.08154 | -42.07714 | 2025-10-16 03:49:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e93f15f3-0790-31da-a3f2-a62aad80da20 | -14.74586 | -42.37608 | 2025-10-16 03:49:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 595a8203-1782-3443-987f-6eecc7ba7555 | -7.39485 | -39.70266 | 2025-10-16 03:49:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 29.7 |
| b7793b39-4389-3c98-b564-ec4e8eb18069 | -7.08351 | -44.94085 | 2025-10-16 03:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 241eab68-2a19-3c8b-835d-e9d5c889495a | -8.26833 | -43.36171 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| eadf3a51-7813-3ed6-ad4f-c8c0b0618cbd | -8.46876 | -44.18543 | 2025-10-16 03:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 8ae532b4-c1b8-356d-82c7-fdd8d5f6b602 | -6.70929 | -44.38167 | 2025-10-16 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f80c8a0d-bc2d-3ecb-9b98-c628dcc93688 | -8.29209 | -43.4307 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 92566cb5-6b2d-3a60-8835-5ba82eab188b | -8.54921 | -44.58283 | 2025-10-16 03:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b289b741-5431-3638-8b98-d9c729e9ea89 | -17.07351 | -43.79161 | 2025-10-16 03:49:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d52f489f-4fc5-3cce-823f-2e0b6b6bfa6f | -8.46948 | -46.21789 | 2025-10-16 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8dc4873e-03ba-3e81-8f6e-2c6db2c09dc5 | -6.54734 | -43.92544 | 2025-10-16 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2a9478d-008b-386f-a814-ae1e77e8af9b | -7.60989 | -46.4738 | 2025-10-16 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b17bff1-deba-33a7-b803-d80911e19060 | -7.96989 | -44.1302 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f67af726-afe0-3f43-bf06-c0fed9793944 | -8.26016 | -43.43579 | 2025-10-16 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e083d66a-8272-3ab2-b97d-c6cf01fccca1 | -9.55549 | -36.8974 | 2025-10-16 03:49:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5da575b8-935f-3068-9a1d-2ef512c5fd27 | -8.46128 | -44.18112 | 2025-10-16 03:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| bb537d50-b224-31c7-aef3-d784123c7be4 | -8.24739 | -44.13799 | 2025-10-16 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d67885a-b73a-3e33-abf3-3612f35bf1d2 | -7.96542 | -38.28228 | 2025-10-16 03:49:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4dadbc3f-68e6-3489-8a49-1243b487f327 | -8.7898 | -38.73591 | 2025-10-16 03:49:00 | NOAA-20 | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 470d76fe-b92f-3ca3-9c36-5763b6a458bf | -6.63093 | -46.83639 | 2025-10-16 03:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f5e7f1b-c4e6-3dbf-a348-9b63ee95447c | -8.45582 | -44.1851 | 2025-10-16 03:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 24.9 |


[Clique aqui para ver as próximas entradas](README37.md)
