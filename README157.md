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

## Dados Diários - Página 157

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7eeccf3-05cf-3475-b7a6-7226861cb1de | -10.07173 | -50.24498 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 8a19262b-6eb4-35c5-80cd-98e5c50a0d07 | -9.89855 | -48.45416 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 88162082-ffd4-3597-991b-a8be6df24856 | -11.79513 | -49.81145 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 091209e7-719e-3be6-a8b8-3be747146a37 | -9.40236 | -48.32441 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ac9bcf1e-6ab3-3eb7-9131-bc9323889a2f | -10.13595 | -45.82699 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54b00b31-6a4a-3798-87f1-fae0efdc3caf | -12.05997 | -50.06434 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 8b34335f-9140-3b50-8d39-cf7631b04ea4 | -8.77628 | -44.30404 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 282babc0-3842-337f-9abe-99cb477a1ca1 | -11.51795 | -45.35438 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ec8074e8-7c5c-35a9-b23c-d8ee4b5ef48a | -10.09624 | -48.43553 | 2026-09-21 16:01:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 861180a7-e277-3278-bd4f-33b904368702 | -8.78279 | -44.28372 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 5e5e3733-9c42-350b-98e2-884572285782 | -9.17005 | -50.02355 | 2026-09-21 16:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| e7c74b8f-5851-3095-9836-f98b7288a31a | -11.67322 | -43.44306 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 894342fe-b270-3f62-9f01-3c0404250b64 | -11.93989 | -46.50679 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 69a6f8c9-a84d-3ed1-85cc-408ac3f979fe | -8.68304 | -45.32532 | 2026-09-21 16:01:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9aa41fe1-6458-36b8-a214-1e129be0e63a | -10.35142 | -50.21175 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| e2a4fd27-2503-31ed-8a61-e32e2c841d10 | -12.30343 | -50.71616 | 2026-09-21 16:01:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 35267636-6179-3fb8-a6a2-daea832de8aa | -11.81747 | -50.02751 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| fe084ede-abe2-34f4-a06c-29b45e73b533 | -10.97633 | -50.5906 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| a4545eed-32a6-3c88-a5be-97453b3cb70f | -11.14835 | -42.79302 | 2026-09-21 16:01:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 179393a0-9551-3a3e-9708-9ebe457e276f | -12.4885 | -44.72352 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| a59b03cf-0eaf-3085-b624-20aba0909265 | -11.44131 | -45.39055 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 4e659ae8-74fb-3df4-a028-13103791c4a4 | -10.87074 | -50.16144 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 50cbc8de-a7ce-3d2f-90cc-169e2b2f5a52 | -8.77021 | -44.30364 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 61.0 |
| b719c401-8ba9-3962-b8f6-337bf7c8811e | -10.80683 | -50.76169 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 05fe5df3-8ad3-3147-b191-d119ac628de1 | -10.38334 | -48.89674 | 2026-09-21 16:01:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 5c60ab9e-dcbf-384f-9a2f-877895c5beb7 | -11.14043 | -42.79803 | 2026-09-21 16:01:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 7bf2287d-9998-35ea-919b-38f2e3af905c | -9.53541 | -47.95956 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 6b4d6543-b957-3e01-9a28-759a14530ab4 | -10.01486 | -45.21673 | 2026-09-21 16:01:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 494dc993-9075-392b-8741-01e0c152d19d | -11.82505 | -50.03317 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| e0086753-998a-3d46-a90d-3459674e90a9 | -10.6992 | -50.67909 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2e796284-fc28-3de6-aa18-0a2cc06cf707 | -11.48218 | -47.64359 | 2026-09-21 16:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 25a22985-753a-3f0e-a663-f5e8cb722c27 | -11.7091 | -42.76198 | 2026-09-21 16:01:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 9322c6ac-2d66-3330-9b9f-a94b0f98cb31 | -12.44113 | -47.06845 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 896e81b0-928c-3d8e-8d81-9884843e8ee2 | -11.29402 | -43.197 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 40786f6e-ac14-3838-bb50-0d3e95bb5455 | -9.45255 | -45.41629 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 261.2 |
| ee3ed4cc-1789-3f96-92dc-433c013695c4 | -10.7679 | -50.60716 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f95080be-efbd-33f7-8ec0-b418c245afb5 | -10.81264 | -50.15054 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| a95fa234-efb5-3620-810e-8c0676671876 | -11.66899 | -43.41189 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 6342d468-a711-327f-87c0-791eda66c9a9 | -10.99697 | -48.23942 | 2026-09-21 16:01:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 4581f099-ec66-3fdc-a71e-5c69fcdb90a1 | -10.35824 | -50.21104 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 3350889d-fe7e-3d47-9c0a-8070f95a1ada | -9.95544 | -45.74164 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 5c6d9025-59ba-3400-9297-2510b4d1d16f | -12.5764 | -40.16058 | 2026-09-21 16:01:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| b6c8f1f4-d811-37f1-addd-d640e586cbc3 | -11.08056 | -49.74722 | 2026-09-21 16:01:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 50f474f2-aa9b-339e-8a33-7356364335bd | -11.43509 | -45.38216 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| bff27dac-dd29-32cc-81e2-a289341910e9 | -8.76801 | -45.87515 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a3e0deac-4e57-3ebf-ae0b-139bb918a48f | -11.6477 | -47.78864 | 2026-09-21 16:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 115ce563-87e0-3342-9fe2-563ed1e62d5e | -9.97029 | -50.26177 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 61b1761a-9471-3f90-9abd-0fbb895c7ed6 | -11.07693 | -49.7382 | 2026-09-21 16:01:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 1b5e8337-de1c-3f8e-b47e-635da6f8640f | -13.43792 | -43.82318 | 2026-09-21 16:01:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 74ac668b-9263-3f41-9986-8103993e14ae | -8.7661 | -45.85485 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 983627c9-c6d1-3662-862d-d497e134142f | -10.82143 | -50.15381 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 035e1c7a-a1ef-353a-9d39-ba54b167354e | -12.42947 | -47.02041 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| cb0cc2d8-0004-368c-b2a6-37e607543c75 | -12.27282 | -50.14983 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 31121a2d-c1e5-3d9f-a8e8-cead3dd38562 | -8.69608 | -45.45612 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 9f9e6977-220e-36ba-915c-c672a732b809 | -10.25584 | -49.99575 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e4ac8d3a-fd35-35e1-96b3-67981807a1ac | -9.01717 | -48.16228 | 2026-09-21 16:01:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f03beaf7-e5eb-3839-8f09-f71eb1827354 | -12.43085 | -47.06806 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2399e282-ef21-35c4-b499-975904be98e7 | -13.55019 | -44.88443 | 2026-09-21 16:01:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b8993a7b-5ed3-3dad-b9af-df666f3488fe | -8.94773 | -49.05269 | 2026-09-21 16:01:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6046e357-1010-36d4-aefb-5ceda9a2d65e | -10.37824 | -48.90736 | 2026-09-21 16:01:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| e95c3388-ecd4-32dd-b54b-fea5514f291d | -10.69139 | -50.67303 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 474d2157-f489-3070-a25d-8f0a257bf1ea | -12.80435 | -44.22495 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 87197b65-3d62-3fb9-98ef-2a6fe43a714d | -11.08564 | -49.75528 | 2026-09-21 16:01:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 46145abb-110c-39d9-8569-5ae14b0b32d0 | -11.1024 | -48.29266 | 2026-09-21 16:01:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 9761c2ca-81cf-3d79-8cf2-0584758394c5 | -12.10408 | -47.05111 | 2026-09-21 16:01:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 0db890aa-7a1a-358c-8202-abbba78baf53 | -12.47063 | -44.6828 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e978b4f6-5656-3487-9ec5-16c436eefa8a | -12.77822 | -47.118 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 86da1518-5895-34b8-994d-865de38b6447 | -11.02424 | -46.54649 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fb9cd8e0-d56e-3166-9881-4ff1e088d2d2 | -10.16131 | -45.55595 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5a9eff77-db2b-32d3-8584-cc60d54dd036 | -11.9347 | -46.50603 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4a4f32b8-d7e5-3e2a-b972-f3276aa8c6fe | -8.78341 | -44.28835 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 4803f2ff-d53f-343d-bf60-b14617381835 | -8.78468 | -44.29779 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 08e2b659-4949-3bbc-9f86-eb3cc3851a8e | -12.04783 | -50.07631 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 2452cabc-72f4-307b-a351-c4f5ac7083a1 | -9.90406 | -48.4487 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 272441db-878d-38bd-b76d-846fd5d93c41 | -12.77807 | -47.11293 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6ec7880e-12e4-3492-9a2e-2107afe4740d | -11.07913 | -49.73536 | 2026-09-21 16:01:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| ecf5c5c1-25d8-3bdb-b973-f001711c3cd7 | -13.05677 | -50.62866 | 2026-09-21 16:01:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e9079737-f65a-3b2b-aa2d-d546bdbf5b95 | -9.61095 | -43.93351 | 2026-09-21 16:01:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 51.7 |
| 91288cb3-13a8-39a6-b93e-f88ab97be93d | -14.1173 | -45.59809 | 2026-09-21 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5c67da66-1dcf-394c-b872-bcd7217c1fa3 | -14.0988 | -44.83611 | 2026-09-21 16:01:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a844e977-19b2-3d23-9462-733c3e85be83 | -11.01827 | -49.73564 | 2026-09-21 16:01:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 13de8533-d261-3170-8ac2-a219020c0a2e | -8.46886 | -45.0821 | 2026-09-21 16:01:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| e580ff56-fcdf-39c7-888a-c914ca91df6b | -12.48525 | -44.72091 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 3ac0e642-d0b9-3d64-81b1-4b18f2b6d95d | -9.6199 | -43.93238 | 2026-09-21 16:01:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 27.6 |
| db8edb44-22ce-3d1b-a595-1f100b48f595 | -11.44409 | -45.3719 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4e21345d-76b2-3ca7-a18b-a00e1226bf56 | -11.14777 | -42.82161 | 2026-09-21 16:01:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 50.4 |
| a1d21d32-ce0a-3ba6-b017-ba610ce4ca4f | -11.43244 | -45.36123 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 3e946078-4aeb-3b5b-8c58-9c523140f185 | -9.89742 | -48.44497 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| b9f36a4e-e14e-37d7-b111-d742bd445744 | -11.55221 | -41.78561 | 2026-09-21 16:01:00 | NOAA-21 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 2ff38ee5-c26c-397c-b22c-0f166fc459cb | -9.98391 | -50.26035 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e508d1a7-8cd6-3eb0-a667-046a82e62f56 | -13.428 | -46.32804 | 2026-09-21 16:01:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4f3e0eba-7acf-397d-af06-bc310bae2a8e | -13.23537 | -46.93398 | 2026-09-21 16:01:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 72eecf72-1e3b-3c98-af2c-1b7e21b281df | -12.44639 | -47.06371 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 7e23f282-0d90-3cb7-b772-e7a51ad043fb | -12.43132 | -47.07219 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3cb7d4da-343f-3380-8cb0-ae1aae5b6c71 | -10.14171 | -46.94797 | 2026-09-21 16:01:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c0ce1905-6651-3b89-8112-5826a412049e | -11.40985 | -47.34029 | 2026-09-21 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d18690e5-906a-3f27-8c78-6164b0539888 | -10.84194 | -50.15174 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 3096743b-e5eb-37c3-9ed2-b746eb432751 | -10.09604 | -45.84131 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 395035fb-b42c-34af-a45a-b0003cf4efc1 | -10.8723 | -50.16002 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 38bc2a91-10c2-3207-ab65-c3a5cfd2edd8 | -9.51176 | -45.8148 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README158.md)
