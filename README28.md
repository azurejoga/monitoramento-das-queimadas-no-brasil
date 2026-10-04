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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90caa2d8-16d5-3b09-be93-aeb905bbdf48 | -6.70845 | -45.97182 | 2026-10-04 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1df084f4-aef7-3765-b9f1-76fc296f7bc7 | -2.58784 | -51.85883 | 2026-10-04 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| eaef1126-6738-3d32-a7cf-51271d6eb3e1 | -2.82975 | -54.11551 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b046c2e8-17dc-3e15-9c15-21be1d5af8f5 | -1.09502 | -54.10494 | 2026-10-04 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| daef1541-4a59-30c6-a602-73255607b274 | -6.72036 | -45.55135 | 2026-10-04 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a16bd279-dc0c-3a07-934b-4611e15c91f6 | -2.57939 | -49.99988 | 2026-10-04 04:19:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2490a608-1a07-3d15-a42e-9363d4cd450f | -6.61599 | -41.5572 | 2026-10-04 04:19:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 618fe7d3-b52c-35ef-8cbc-23f05ac86868 | -2.88378 | -54.14 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bc18b80a-968e-30d2-95da-b9595b6ac08b | -3.0797 | -49.53008 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a99a858-9619-3fe0-8b71-aef61e1d361e | -1.40548 | -49.26485 | 2026-10-04 04:19:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e37245b5-20e1-3064-b616-88366aebe7c3 | -3.12208 | -53.71829 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 4d9cc151-ddeb-3179-add8-9f1d92d974a7 | -3.27284 | -50.08909 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33512cf7-5c2e-376c-a806-f3e4318e0d21 | -6.5705 | -44.15707 | 2026-10-04 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 310c5c47-1d9d-3962-a7e5-eb718c8d77a4 | -6.28075 | -53.15268 | 2026-10-04 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09406d2a-dbe0-3518-a755-fd85e551dd1c | -3.10873 | -53.73089 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a85e1ca1-9515-3be9-b84d-56661376af23 | -2.9991 | -49.22239 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d55218e2-0761-36fa-bc70-3abd27a732d1 | -7.01236 | -47.5285 | 2026-10-04 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f78995a-638c-3002-af19-6c961371fc86 | -6.38492 | -45.80172 | 2026-10-04 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64b0bd9d-e9ec-3ce9-bf83-e0b10bdc83c4 | -3.87186 | -55.80415 | 2026-10-04 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 11c76242-ea98-338a-a446-9c3c0c0eb85f | -6.92829 | -44.45845 | 2026-10-04 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cdb54b1-e42c-34e3-b296-4522fe47d508 | -3.11541 | -50.28157 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7ee9570-1d1d-3095-8cdf-2604f429c357 | -4.15926 | -47.53384 | 2026-10-04 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1be78045-c91a-3958-8e96-e44ecb47aec5 | -5.99435 | -53.63865 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53ecc76b-3952-34cd-a709-d22583d0d0f0 | -3.1693 | -48.58479 | 2026-10-04 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c34f766a-737c-3f5f-afc4-c725dda5e505 | -4.27856 | -50.28101 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 84793b0c-61da-3279-98bb-aeebb24b29a0 | -2.85213 | -51.28867 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a6f2bde1-c335-3936-b648-94cd84923f45 | -4.28545 | -50.26589 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 375.6 |
| 3cd223e2-84d4-341c-8eb6-ec1639c7733e | -5.86736 | -50.15741 | 2026-10-04 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b03f4f7e-e04d-3a88-9c6b-c3fa77967a39 | -4.05889 | -54.313 | 2026-10-04 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2b44ff8e-63f9-3a10-84a9-f9c22150ae4f | -3.35299 | -43.38577 | 2026-10-04 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cf9a4ff-ef71-3824-9a0e-4c4cfdd5cbaa | -4.29197 | -50.27913 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8eed0d11-47d9-3359-aa78-279a64bd596e | -2.80456 | -54.12723 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c7d1a2b9-2674-37c4-ac3f-d17c979113a8 | -2.58267 | -51.87788 | 2026-10-04 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 94d70725-e6ea-3e45-9740-04daa9caabf5 | -5.82823 | -53.50455 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab3c3d1f-561d-3e52-aad7-78add814d822 | -2.59442 | -51.84887 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 46094f83-a2ea-3a3f-8b0c-9dc6712b963a | -2.75568 | -51.55076 | 2026-10-04 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c032e7df-be0b-39ea-b780-0c84cfa13c2b | -3.86992 | -55.80881 | 2026-10-04 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| e8018085-c230-39b5-9874-4d8cd6a97015 | -4.01971 | -44.82605 | 2026-10-04 04:19:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 726d8834-18d5-3577-8c46-06fd5a5fe3dc | -3.36294 | -43.3873 | 2026-10-04 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c0a830bd-de6c-3f3d-88b4-1bb845322598 | -3.6991 | -50.66341 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8ab06070-0792-3d12-8a33-d74efd2f5bb6 | -6.94371 | -41.97153 | 2026-10-04 04:19:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f1b2cb5d-f50f-3d03-bc2c-9db9191b465f | -3.89176 | -49.69617 | 2026-10-04 04:19:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 930173f6-8922-3a23-9010-d26cf55fa9de | -3.08439 | -49.52709 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c7d6bdf-f52d-3a4d-8668-a966814095a1 | -2.84666 | -51.29282 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 82176c8c-48c8-3b53-9087-88802f887534 | -3.18888 | -54.10413 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 122dcf38-4eed-3a56-ad4a-2c482bcc0c4e | -2.811 | -54.08875 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c78676a-9547-3033-9860-8b8b8497ea99 | -3.4653 | -50.10563 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 357e6bc0-a824-37b7-bbed-7f80a7100ca6 | -3.28116 | -53.81973 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a86ab17-8d96-379d-8ef2-253db4dbd3bf | -2.83184 | -54.20855 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd50743c-9642-3514-8378-c3043ffd9f0e | -1.1715 | -49.26356 | 2026-10-04 04:19:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 170042f3-a114-39b7-bf22-1a2eafef5c3d | -3.0691 | -49.54363 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c3c27479-f59a-321a-aa92-73de69e63409 | -4.28121 | -50.26519 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 375.6 |
| d2d51bb8-2c9e-3bda-92da-ea4c17ea01b3 | -3.07853 | -49.53749 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b14ad4b4-4015-3649-8558-238f7c90f7dd | -4.27125 | -49.98105 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92492bb7-efd8-3ef3-b6af-aee465773e94 | -2.92232 | -54.10047 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e6c0cf2-0003-30c0-a56d-3300c9899dab | -3.17521 | -54.08213 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2d99ba7b-94de-3a75-87f5-59347d78c821 | -0.33368 | -52.04097 | 2026-10-04 04:19:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b9d66b2-3de5-3668-b67d-83123c9c8258 | -3.81406 | -50.84628 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01afc8d5-65fe-3594-90dc-56e290938b16 | -5.73927 | -45.14397 | 2026-10-04 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91e63ac4-7b92-3903-9adc-708f10c53d1e | -6.02459 | -43.5937 | 2026-10-04 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd4b4b79-d89a-3210-8a49-163b698db659 | -3.96411 | -55.77926 | 2026-10-04 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d99c96c-6714-3699-9d5e-4d04bfe06366 | -3.10607 | -50.28434 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9fbe6a4-622b-30a9-b979-e230b99dd111 | -3.87105 | -55.80894 | 2026-10-04 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| e419ddff-beb9-35b8-98d1-c49b3af1abdd | -6.0799 | -53.48317 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79aee4ea-2f0e-3548-a56d-1cce33bae888 | -4.28414 | -50.27377 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 8b473998-85e4-30ed-9c2a-d8190e772574 | -4.28252 | -50.25732 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9b2b7922-4903-3590-a5cd-15e055ceeeeb | -2.79583 | -54.11003 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 03dfdd8a-3297-36da-b01b-02b0ab9ac85b | -4.26154 | -50.78788 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e439f54-193f-327b-b800-9795555e9e8a | -5.74044 | -43.27267 | 2026-10-04 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a1babe2-20fe-3d46-807d-6c2e13f615bc | -4.50316 | -45.99566 | 2026-10-04 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b58cbe04-0753-3547-b0ca-a614d03380ef | -3.13127 | -53.73084 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c7464b6f-7451-3bc9-9158-37048dd87cdf | -5.5475 | -49.76205 | 2026-10-04 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 13f18673-9dd7-3358-aa72-ef9f30a35df8 | -2.80842 | -54.10415 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 76769f49-d762-3841-84c7-56fe6f0afdac | -2.36667 | -50.60371 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0177ea01-4216-36d9-b502-425ad2e43e5b | -6.38837 | -49.80952 | 2026-10-04 04:19:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7089d1c4-07fb-3636-bbe1-d35440755942 | -2.754 | -51.56083 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 910912b1-35e4-33d2-9af5-712535f4e8d2 | -7.47848 | -47.60549 | 2026-10-04 04:19:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| edfbf4d2-e05c-3eab-83b1-98d0895481d1 | -1.12381 | -54.14823 | 2026-10-04 04:19:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec5e4156-286b-3ba3-ae2a-8faeeb07b99d | -5.05003 | -42.78566 | 2026-10-04 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7999ac46-b8fa-3ba3-b422-eca744ece0c9 | -3.09524 | -51.09688 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 726d81f7-a6a2-3f60-9a53-1f224a7c56ac | -2.80986 | -42.31025 | 2026-10-04 04:19:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21d78b39-67e7-3c17-82fa-aa9e977e4647 | -2.8178 | -54.11752 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 05859dc3-7a6f-3213-b526-d1e95e27411f | -3.89588 | -49.69674 | 2026-10-04 04:19:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 001aafe2-a626-3e6a-9e48-c57541af34d6 | -1.21038 | -55.85994 | 2026-10-04 04:19:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c1e05559-31e1-3569-ac64-5d9a66dee8e4 | -7.00951 | -47.52405 | 2026-10-04 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 900a6b4f-c5f4-3459-ba23-1e9b3fa9ded8 | -6.42166 | -43.46851 | 2026-10-04 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6bc33988-d8cb-3dc7-8005-7a63c9ff7f3b | -2.94605 | -54.132 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d76d7940-701f-3c30-b2b8-cab3fadd7edd | -3.81821 | -51.5433 | 2026-10-04 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8796c1ea-fdab-3b8c-812f-7da31960be13 | -4.25798 | -46.37291 | 2026-10-04 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 60737ea7-c8bc-3da8-bbc5-769150636937 | -1.01299 | -48.79437 | 2026-10-04 04:19:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c113ddf-17c4-3c4f-8a87-70089a49ac46 | -2.9542 | -54.11771 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5116769c-9da7-31a1-b71e-7ed951cc69dc | -2.82409 | -54.11459 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 83fac010-e1fc-3ff3-9883-547ed897d16a | -2.82783 | -54.12707 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bb71bc67-340c-3b0e-8ead-ff17a290d314 | -2.85133 | -51.29354 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 27805aed-2c0f-3933-8842-582eb013a236 | -3.28552 | -53.82742 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11d8586c-0d2d-3d70-abd0-e6bdea260438 | -4.96741 | -47.97459 | 2026-10-04 04:19:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75a97166-f218-3261-8191-a97051664c22 | -1.41379 | -49.26611 | 2026-10-04 04:19:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18782f07-0330-3552-88d8-ca950dff91cd | -3.47021 | -50.10234 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e50a13db-20e9-31e4-8fdd-a8f2e35e04a6 | -5.99812 | -53.52661 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ddc612c3-f3db-3af7-b878-1de2b34e6f69 | -5.54771 | -44.21388 | 2026-10-04 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README29.md)
