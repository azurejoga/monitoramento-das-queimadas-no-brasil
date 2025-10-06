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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08e53bc2-4538-39c1-a0b8-eb88bc808815 | -13.343 | -48.0519 | 2025-10-06 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 54a43a55-aab9-388c-a333-edb8ccb908f4 | -7.7935 | -42.5845 | 2025-10-06 13:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| 4f69a6e1-c2dd-3ca3-a19a-e23aa2944170 | -8.6144 | -46.2778 | 2025-10-06 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 213.8 |
| dd037a25-5061-3cec-85d8-cde2d94eedb5 | -7.2778 | -44.7778 | 2025-10-06 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 1bd5f046-108d-383b-9823-9b2778438f56 | -7.7885 | -44.5228 | 2025-10-06 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| e6ed2f58-170a-3c46-8876-39001a02f8df | -6.8388 | -45.4753 | 2025-10-06 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 9c7218e3-8978-39ee-80a7-a51c450b1789 | -8.1873 | -44.2746 | 2025-10-06 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| b96ac420-6d07-3447-b13b-742e523b1b3e | -7.0372 | -42.7563 | 2025-10-06 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 75.0 |
| 2821609c-fa10-3c0d-8f69-a347490bf4e2 | -10.386 | -45.4184 | 2025-10-06 13:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 192.8 |
| a72858b9-9502-3cf2-baeb-ef5a47696e87 | -8.0678 | -44.7929 | 2025-10-06 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 06d9f5b6-4709-366d-8fe5-063a68ffadc6 | -17.8417 | -57.6254 | 2025-10-06 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.6 |
| 91d77058-4e0c-39ac-87c9-1d0116536a04 | -8.6327 | -46.3208 | 2025-10-06 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 1d10cb05-f445-323f-9c3d-0f86f2b0765a | -10.3724 | -50.3149 | 2025-10-06 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 0fe0b48e-22ed-39c8-b55c-bc5719804f36 | -7.2392 | -44.8727 | 2025-10-06 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| f9d43dda-51b4-3b97-be9d-96a55df12d0f | -12.4464 | -45.5876 | 2025-10-06 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 85cae869-7a11-3769-b4d0-1b0375b912c7 | -14.5442 | -46.9405 | 2025-10-06 13:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 65.7 |
| ce71d76c-33e8-3716-bb06-21d6871e1256 | -12.5929 | -48.1144 | 2025-10-06 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| a206a2d6-ccb7-36e2-a950-fc0dd405f9c2 | -12.1267 | -50.9545 | 2025-10-06 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 30aa37df-157a-3f05-8da2-a2f7678c98c2 | -7.4279 | -46.5016 | 2025-10-06 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| d5881a15-1915-3fe5-b537-f39ffdf62198 | -7.2723 | -45.2792 | 2025-10-06 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| b3b6ab46-7a0a-3adb-bf94-76d1b982a347 | -14.6135 | -52.495 | 2025-10-06 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 41bbd8f9-5160-3209-8920-03870060e061 | -8.1055 | -44.7891 | 2025-10-06 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 121.5 |
| acdfec1e-02ec-3e0a-98c8-ed822bd86de6 | -7.0369 | -42.78 | 2025-10-06 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 98.1 |
| 93dc4635-a20f-39f6-b3fe-c86d43a727fb | -11.8029 | -45.1087 | 2025-10-06 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| d3a4bef8-3cd6-3450-b403-5500e4b27010 | -14.8828 | -51.4777 | 2025-10-06 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 307.0 |
| b735bf88-076e-33b7-972e-ecc64eb11b68 | -17.8617 | -57.6024 | 2025-10-06 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.6 |
| d3222253-c521-3327-b9f0-89e76dc127b3 | -8.5581 | -46.2611 | 2025-10-06 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| d8669131-8930-3ac2-a398-4388647eacf3 | -17.3816 | -53.5947 | 2025-10-06 14:00:00 | GOES-19 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 8edce56d-b54c-3d1e-8da5-e9355f36bbc9 | -11.0104 | -50.6744 | 2025-10-06 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 130.2 |
| a1cc757f-373c-3f8f-ab79-92bfc417c566 | -11.1185 | -47.2207 | 2025-10-06 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| e08b7212-9370-3c93-80e9-adb6f50e96fa | -12.1458 | -50.9523 | 2025-10-06 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 6ca1c48d-0cc6-38bc-8232-c841f07573e1 | -7.2778 | -44.7778 | 2025-10-06 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| a578b1eb-1851-3780-b7c1-0a94aea96813 | -12.9841 | -51.0648 | 2025-10-06 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 6a7251cc-599f-32a9-adbf-2aa66cd8b210 | -8.2071 | -44.2032 | 2025-10-06 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| e9055ad7-5782-3d83-b2a1-0c8b73bb8fbd | -9.9018 | -50.2341 | 2025-10-06 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| ea5596e9-fcf2-30b9-8d15-a46566d79917 | -7.4281 | -46.4793 | 2025-10-06 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 3ae046e5-979b-30cd-95bd-e8aab77906b3 | -9.3162 | -46.0005 | 2025-10-06 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 582f9d79-df15-3a92-a16f-b544a78d5a2a | -7.2723 | -45.2792 | 2025-10-06 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| e0fdf160-0fc8-3eb9-8089-8f6c7b430c85 | -7.448 | -43.0693 | 2025-10-06 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| 48379f05-0805-325f-85c1-740ed009e25e | -6.6303 | -45.7178 | 2025-10-06 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| f39a3cb8-2191-3304-b822-0cfc0a376e2c | -7.4276 | -46.5239 | 2025-10-06 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 93edb050-961d-367a-81db-eacacda84b3f | -9.9054 | -49.956 | 2025-10-06 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 3ff9616f-6a09-3354-90de-f4886c259853 | -7.8074 | -44.5209 | 2025-10-06 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 110f21b5-7e0a-3ef6-8451-8094d92def0a | -10.386 | -45.4184 | 2025-10-06 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 255.4 |
| d697abbd-17c7-33f3-8210-742ec8caa56d | -14.8828 | -51.4777 | 2025-10-06 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 245.0 |
| e8a5f148-dd4b-328c-86d4-1da0a24309b4 | -13.0033 | -51.0624 | 2025-10-06 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| c3af55fb-658a-3fe6-a23b-d2c9f756bd4e | -11.7029 | -45.3536 | 2025-10-06 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 4dc9beb2-dc1f-3300-b030-2af7ad1c7a07 | -13.0779 | -47.8234 | 2025-10-06 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 3d226a6e-4663-3061-b386-caabf5e89689 | -10.7281 | -46.6433 | 2025-10-06 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| f5eba358-d3dd-30d4-b0bf-e3e98089a299 | -11.7573 | -51.5059 | 2025-10-06 14:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| e770ff0c-1879-3fde-8087-70ea26dd3995 | -9.3165 | -45.9779 | 2025-10-06 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| e6efd6c5-3c16-3e90-95e0-ff76fde0f322 | -8.6139 | -46.3227 | 2025-10-06 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 3b899269-4236-3ac9-a43d-fad48d294c46 | -7.4279 | -46.5016 | 2025-10-06 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| cf59a036-ee52-371a-b982-c49709fa9718 | -10.4054 | -45.3931 | 2025-10-06 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 7920bd26-ba00-3ca7-b762-0065e7728b67 | -13.2515 | -47.7979 | 2025-10-06 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| a8c9fac8-8849-3d99-979e-57d38ee3974a | -11.8447 | -44.9176 | 2025-10-06 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 7d6882af-60e4-38c6-841c-c5c607362bbb | -11.8029 | -45.1087 | 2025-10-06 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| aed175d0-bc70-308b-915e-22630fd49a22 | -6.837 | -43.8511 | 2025-10-06 14:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 8f2f7d07-c564-3af4-aabc-4732b45324e0 | -7.0572 | -44.3393 | 2025-10-06 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| ac05d5bf-ebcd-358b-a62c-e142e2e5a0bc | -14.6325 | -52.5137 | 2025-10-06 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 164.1 |
| 1057a8fb-0bf2-3f3e-bfec-ec68c8a2e2d7 | -8.0678 | -44.7929 | 2025-10-06 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 17dd56fa-c671-3665-b644-0cb1c60e1db1 | -11.8234 | -45.0364 | 2025-10-06 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 76b155bc-51da-3f6e-b749-8c263b0f1588 | -10.7285 | -46.6208 | 2025-10-06 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 8a11d937-0854-3dc2-932d-45c23e1b349f | -7.2091 | -45.9167 | 2025-10-06 14:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| c005266b-0b15-3932-9248-e4f2191c92c1 | -15.3541 | -47.3235 | 2025-10-06 14:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| af8c44c7-538e-34e5-9754-781f9cdb0b78 | -17.8614 | -57.623 | 2025-10-06 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.8 |
| 5a1bfb2a-b1c5-37af-850b-702b7acb9076 | -7.0369 | -42.78 | 2025-10-06 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| d09b4607-e6d5-36e2-bd6a-c633469086e7 | -7.7203 | -42.4023 | 2025-10-06 14:00:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 112.2 |
| 610ba49e-f4d5-34c9-b8ac-074a6c380063 | -7.4672 | -43.0438 | 2025-10-06 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 316a9b50-62fb-377f-aa49-10365f8609db | -8.9472 | -49.8545 | 2025-10-06 14:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 4dd40e94-aae1-3b54-a095-bcc9b2d53097 | -7.0367 | -42.8036 | 2025-10-06 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 65.2 |
| 8249892c-f0cc-3d9d-8c0e-b1621d18fc14 | -11.7912 | -48.0448 | 2025-10-06 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| ad22c0b0-2264-31cd-9857-c9d5056d15c8 | -12.4665 | -45.5386 | 2025-10-06 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 836ae111-0f70-3337-b909-b5fad640b214 | -17.8417 | -57.6254 | 2025-10-06 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.2 |
| 2b5d5dac-35e4-3d8c-9cdc-fdd7938fd858 | -8.1882 | -44.2052 | 2025-10-06 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 129.5 |
| cfcf2693-ef6c-3c80-97ad-341efcb990c2 | -11.9327 | -46.438 | 2025-10-06 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| dfc0c0e8-448f-3ff2-852d-2e70e6561e6d | -13.0763 | -47.9127 | 2025-10-06 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 3cf0b311-cf25-39de-99a0-cd66c7f03287 | -7.3101 | -45.2531 | 2025-10-06 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 10de389d-3cd2-316b-b990-17f851781f14 | -6.8456 | -44.8162 | 2025-10-06 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 9543d8c2-9f48-3b88-8f79-3eaddbccdc11 | -7.7743 | -42.6103 | 2025-10-06 14:00:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| f29ddbf9-3fb9-35a0-bcd3-110e9371c776 | -8.539 | -46.2855 | 2025-10-06 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 6763ba9e-0722-3977-a4eb-da0586fa8414 | -11.5058 | -43.5189 | 2025-10-06 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 3c692838-3e4b-3a31-8b9f-d7cfbcb2ab75 | -15.5704 | -47.2625 | 2025-10-06 14:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 77903571-2f16-3b57-a67f-14742c8e12bf | -17.842 | -57.6048 | 2025-10-06 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.3 |
| 58edaa15-e64f-3cc0-8ff5-492d947b4dc1 | -12.4853 | -45.5587 | 2025-10-06 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 995bda9d-a449-3f39-a621-ae5ba95dc6b5 | -7.2776 | -44.8007 | 2025-10-06 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 1003b44f-2ef5-3c61-980d-73af7673560a | -7.0372 | -42.7563 | 2025-10-06 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 72.5 |
| 7787db92-c693-32a0-93b1-3c4d576a74b6 | -12.9844 | -51.0433 | 2025-10-06 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 04e8431e-42f8-367b-81be-7c91cf5ac828 | -11.4421 | -44.9535 | 2025-10-06 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 6d25e509-7c63-34ac-bd28-28d04af34111 | -23.1972 | -45.6306 | 2025-10-06 14:00:00 | GOES-19 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.1 |
| 4e3233e7-c452-3e85-a84a-94013aca08db | -8.5387 | -46.3079 | 2025-10-06 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 11bcead8-dc07-3581-b04e-e80931cf47f0 | -7.4669 | -43.0674 | 2025-10-06 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 142.0 |
| b2a86f8b-f790-3f8e-b52d-2c051465988b | -10.158 | -45.4244 | 2025-10-06 14:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 01aabf1b-3675-3a60-a3b6-db34383c6719 | -16.0083 | -56.0155 | 2025-10-06 14:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 28084848-a173-3beb-a242-2b9903094a70 | -8.6138 | -54.976 | 2025-10-06 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| ac07f772-6526-3bfb-8050-bd96f30f3d80 | -14.5442 | -46.9405 | 2025-10-06 14:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 20bf8fde-b011-39ea-8b71-237181b38b33 | -9.6614 | -45.6667 | 2025-10-06 14:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 208.4 |
| 4b2a5164-5138-305c-abc3-09f283ac0988 | -14.6321 | -52.535 | 2025-10-06 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 601c8338-9ae7-3871-a403-6fa42b09f51e | -14.8637 | -51.4589 | 2025-10-06 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 96a0e272-4c56-32ef-b261-7b5bb27f18a3 | -9.9779 | -48.7405 | 2025-10-06 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |


[Clique aqui para ver as próximas entradas](README93.md)
