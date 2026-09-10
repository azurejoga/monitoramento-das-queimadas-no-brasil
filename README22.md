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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db59287d-e4ab-393d-af29-be2ae1784dc3 | -7.5746 | -45.67718 | 2026-09-10 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09e07dad-298e-368c-a49a-10a7acae6ccd | -6.82636 | -58.9976 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64721e5e-ac24-3b23-9f45-06ef30ff11be | -6.89934 | -52.19304 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9f0022b-4ae8-396f-82cb-b75553e99a9f | -9.71336 | -43.40472 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 84bbcb75-799e-316e-a930-6d33139983f7 | -6.14617 | -51.75358 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fba7f22-43e4-3ac8-89eb-f9e02614b74c | -7.11354 | -42.12329 | 2026-09-10 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d69ed8fa-9461-316b-ba12-12104b1b569e | -6.11524 | -45.38942 | 2026-09-10 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f19327f-0a8a-3a1f-9447-49b4f5e22b3b | -6.24784 | -51.68019 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f424e085-ddc0-3a48-accf-2a996b4d3f70 | -6.79292 | -58.90263 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27126a85-9e45-34e5-89ab-5efee3e6787e | -9.68395 | -43.45895 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 80af7bd4-6e0e-3a8e-9a40-933e1d59d88d | -2.91994 | -54.11346 | 2026-09-10 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da4eaf30-0e54-317d-af91-7d9e055c92c6 | -6.16593 | -44.64272 | 2026-09-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9e7ca922-9b6c-3329-9e38-b5ca4b32deaf | -6.16771 | -47.07817 | 2026-09-10 04:25:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d35ff0b7-b437-38ef-b2c8-e46a280f162a | -5.6267 | -45.8727 | 2026-09-10 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5381091d-e237-3421-bc97-52f07a38ecf6 | -7.14933 | -46.95523 | 2026-09-10 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a04530e0-f902-378c-bc7a-dd6d0afc25e0 | -4.82922 | -55.76245 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91d73810-3122-3322-ac05-1c2ea092ff20 | -2.72417 | -57.6214 | 2026-09-10 04:25:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a4ea38b-f647-3f1e-a002-97533acc1cb1 | -6.17103 | -43.01892 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7157ad35-e3c6-3f3f-a5ec-ee9275013521 | -6.75644 | -58.96151 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 56d009ac-4748-3170-a6ae-3cb1e37e7bca | -9.71855 | -43.39378 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 146f52a8-385a-3b3c-9638-216f2f059e79 | -6.3302 | -43.81487 | 2026-09-10 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebe74add-d941-3437-802b-1092dca41e44 | -4.85546 | -56.00922 | 2026-09-10 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a28d30ee-9691-3a39-8fe1-c4c3c2cb6d6b | -8.31633 | -45.1125 | 2026-09-10 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5bec017-2b69-3489-bc05-cab4faa89cbc | -7.20321 | -43.6348 | 2026-09-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 490fe5f6-5bce-38c7-aafb-dc9bdf7d85fc | -7.18969 | -43.61056 | 2026-09-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abbcbb77-268f-3d1a-a413-e0abe7c0b06c | -3.24822 | -50.82333 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 26dc023b-4347-31e4-841b-a0c44f9db6ef | -4.14977 | -43.10323 | 2026-09-10 04:25:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e5bb867-8671-3dbf-a429-a88b90f1fefb | -9.68336 | -43.43933 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eeb156e9-8e74-3add-9f1c-234a6784b661 | -9.01683 | -44.84804 | 2026-09-10 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7c467e41-df83-3c07-b845-32f3a126b4dd | -5.76239 | -45.08801 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 2dc4380e-b051-38eb-be6e-0a3d281e7172 | -6.79094 | -58.89553 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fe6a1db0-bd26-30ca-9ec9-1f93129a9cdc | -2.10475 | -46.90534 | 2026-09-10 04:25:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4eafefc0-ecbe-356e-86d4-db122841722c | -9.24086 | -40.50109 | 2026-09-10 04:25:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 067ae778-af85-3a81-a37d-6e57823ab101 | -5.77827 | -47.17118 | 2026-09-10 04:25:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b68129c-72fd-3692-97dc-ff7c8f455f91 | -2.91931 | -54.11729 | 2026-09-10 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6eba8acf-13ee-3a1c-85de-199da15f9a57 | -7.97673 | -43.98217 | 2026-09-10 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3344d787-1c6a-39dd-a677-0a867d2a544b | -4.17071 | -42.43428 | 2026-09-10 04:25:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a44522fb-5adc-3d09-bdc1-d8fce6d80c72 | -5.77011 | -45.08213 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a6fb145d-ddac-3227-b6f2-c9ab643e1fdf | -8.23807 | -44.74651 | 2026-09-10 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| b2769195-3698-3143-8db7-a2a20ee42417 | -6.77874 | -58.89981 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6a00cc6-fed5-3dea-8385-678cadb2ae9f | -7.50605 | -45.27425 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58fc31df-9f15-330c-b5bc-af70669f72b2 | -5.76459 | -45.07417 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a9728ec3-21f3-3e65-af12-4d55fc84b088 | -6.80292 | -58.94986 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d3c19fe-b186-3340-be06-2aa3c7518216 | -6.81805 | -44.66408 | 2026-09-10 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e306871e-f055-35ed-90f5-87cf2d1f038b | -2.47664 | -49.40825 | 2026-09-10 04:25:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fded1a13-4bcd-3c00-bf1e-d84204335afd | -7.18632 | -43.61003 | 2026-09-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2eec6810-2682-35a4-a315-6b3202071300 | -2.93628 | -50.4659 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7165e78-5209-3f52-8474-c0c45124860f | -6.26859 | -46.36789 | 2026-09-10 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ada9205f-51ac-38a2-96c8-d947e2161763 | -8.25448 | -42.89474 | 2026-09-10 04:25:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 81189339-9d5b-37b2-a7c8-84d2697a8c9e | -8.97659 | -44.97426 | 2026-09-10 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28f40305-1906-3298-ac40-e7273a7ab1d1 | -8.947 | -44.40344 | 2026-09-10 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b145346c-f740-320b-bcc2-decf8c478c95 | -5.59174 | -45.37037 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de945cdf-e261-3653-bae4-5156796b3f3d | -5.59451 | -45.37438 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69f7964f-b9bf-31c9-a005-b8aa6698d260 | -7.52679 | -45.01463 | 2026-09-10 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad141faf-c509-3f4a-a0df-4901895d43af | -6.49608 | -47.59173 | 2026-09-10 04:25:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 319b321f-cf25-36a2-8ff8-29edcdac0781 | -6.67325 | -43.43906 | 2026-09-10 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f73f2e6e-7945-3e49-a8aa-5294b800e75b | -5.77066 | -45.07867 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 10ed28be-16a3-3791-8b4d-9730e94f4539 | -6.7051 | -45.46236 | 2026-09-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15c73ba6-a262-384d-95d3-1d899a5ce24e | -6.67381 | -43.43545 | 2026-09-10 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f175c36-fcf4-3a51-818b-f5fecdb4567d | -6.78585 | -58.90111 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d4f7f1e-44f4-38e2-9487-f83894920f36 | -6.24409 | -51.67471 | 2026-09-10 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e19446b7-cffc-3e7a-8c22-1abb0a7eb463 | -6.76363 | -44.5776 | 2026-09-10 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fcedd658-6cde-38d7-acc3-3b47d780965a | -5.76846 | -45.09252 | 2026-09-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| d586dab1-37ea-338f-b74b-9e80a4d41ae6 | -9.782 | -43.45797 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb091343-f296-3def-8212-730082dbd5fa | -7.51541 | -45.25798 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f842a9d-2f7a-31da-9ddc-2193ef587e51 | -6.45546 | -54.70734 | 2026-09-10 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd9ad4ba-ffee-3cdb-a0d7-e49daf61cda8 | -7.98009 | -43.98269 | 2026-09-10 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51b9e76e-87d5-3e41-a915-57caf42882e2 | -6.78723 | -58.89398 | 2026-09-10 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2743f9f-5c52-3c9e-a7a3-9d02f20054da | -9.33578 | -45.64606 | 2026-09-10 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cddb88a7-202e-3456-b3ce-928f854e17d6 | -7.47851 | -46.67651 | 2026-09-10 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70176f1f-3480-3562-8e91-4d02346455cb | -5.68901 | -43.39521 | 2026-09-10 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5541de77-6dd8-386f-8081-f3b93cc5ccf4 | -7.27063 | -44.61512 | 2026-09-10 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc9bc450-181f-3013-b780-a20e21004c4f | -7.48895 | -45.27508 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00eae2b3-1d1d-3562-b110-ed1941b8c0fd | -3.55012 | -48.18464 | 2026-09-10 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2591c15-a9de-3c28-b9e8-682aee5d9baf | -4.16728 | -42.43374 | 2026-09-10 04:25:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| da11e607-a770-3298-becd-a23a0ce8d150 | -7.19647 | -43.63374 | 2026-09-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ff276d5-b2f2-3caa-aa27-db98b19d5ff7 | -8.23697 | -44.75349 | 2026-09-10 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6e4d2c2c-638a-346c-9977-baac876e61b6 | -7.11402 | -42.14413 | 2026-09-10 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6747c862-1a04-3909-a180-1e7430dae4e7 | -6.16978 | -44.63978 | 2026-09-10 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ddc47551-5fff-386b-8dcf-7c69a5a7be1a | -2.93709 | -50.48854 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4994f70a-1c49-3e1a-8eb6-e0b6dfa16bec | -7.05081 | -42.71935 | 2026-09-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b1fd602d-629b-36d1-bab1-2e1e392f83cd | -3.37486 | -50.40516 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0f72b41e-ea33-31e2-8345-921721503a3d | -7.99294 | -43.9663 | 2026-09-10 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4cec643-c3a4-39b2-bc71-d72d1a56928d | -6.51076 | -43.96184 | 2026-09-10 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 627badca-0423-3ea1-a80d-ace62459b999 | -9.535 | -45.46051 | 2026-09-10 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b18d39ef-d539-304d-8ce6-c481fdf1f97e | -3.9599 | -44.34973 | 2026-09-10 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8993a0de-fe72-35fd-ab67-6b2faced025c | -9.67936 | -43.48946 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4814c92c-c74d-3869-8ee6-6b69c46743c9 | -9.7226 | -43.39049 | 2026-09-10 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| eae06fca-f765-3fa3-9a5c-d62fd846bea8 | -4.29595 | -49.08747 | 2026-09-10 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 494e02a1-9245-3478-83af-696c1ca0a3ea | -9.30202 | -44.34885 | 2026-09-10 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f6c5728-7088-3c62-a2c7-4cd5f796cd5f | -7.49281 | -45.27214 | 2026-09-10 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10feab57-b833-39b6-8c8b-5bae029cfc02 | -6.77007 | -58.61926 | 2026-09-10 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00f03a82-560e-32f9-a4fb-84193d0ac27d | -7.04446 | -42.71442 | 2026-09-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 48c67b26-19a2-3b31-acae-d4bab92eeec1 | -5.68509 | -43.39827 | 2026-09-10 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07363f24-0eb4-32f1-80ea-7e29ded3a616 | -7.98681 | -43.98368 | 2026-09-10 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 314d8bd6-a277-3f3b-bc6f-034ea158887c | -6.17055 | -47.08254 | 2026-09-10 04:25:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8d30c2b6-4691-3bf1-8199-371631d3991d | -3.15623 | -48.60839 | 2026-09-10 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ce42240-ead5-38e4-8c7e-9484eff87ddd | -2.93413 | -50.47894 | 2026-09-10 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 026cddc2-efd7-3ea5-9348-acfcf7b42d68 | -9.33523 | -45.62811 | 2026-09-10 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7d922c6-3e11-330d-b41e-64c50437e867 | -7.14228 | -42.10263 | 2026-09-10 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README23.md)
