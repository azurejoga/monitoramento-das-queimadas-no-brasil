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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 191133f5-74ca-3e1a-8d03-eb4ea8dce645 | -8.947 | -44.409599 | 2026-09-10 00:28:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b252ce97-aab6-3412-88ef-c8e6cf19de79 | -11.8728 | -44.849998 | 2026-09-10 00:28:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f9793d16-d253-3652-b954-4e4a96451429 | -7.9834 | -43.945599 | 2026-09-10 00:28:00 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d843020a-128e-37d5-9c19-5c7420608b4e | -12.3473 | -48.192402 | 2026-09-10 00:28:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e411f5d-c3e7-3c6f-be6b-a55719e79cc8 | -12.8614 | -44.343899 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a20782d8-e707-33db-af1d-0a61fd719efa | -6.0973 | -44.134701 | 2026-09-10 00:28:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f07c1b9-ecb3-3823-b16a-90fa93987084 | -6.174 | -44.644402 | 2026-09-10 00:28:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73e4d7e7-2d53-34e3-a760-5dc805c1d152 | -6.4602 | -46.298302 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b5b49fd-614e-31d8-ab01-8992090a3d04 | -9.6825 | -43.4837 | 2026-09-10 00:28:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 09b9679d-0c54-3d15-99fc-8b5bd0b6b522 | -10.7501 | -45.952599 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f11f260b-0502-36fe-ae6b-02ba259d3ead | 0.2579 | -51.488701 | 2026-09-10 00:28:00 | METOP-C | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| bd4adc97-80db-3458-a7a9-1a028256cd37 | -10.0657 | -45.473 | 2026-09-10 00:28:00 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9b59dbce-a9b5-372e-a71d-e318458f2571 | -7.9965 | -43.957802 | 2026-09-10 00:28:00 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4bcdade4-8f81-31e5-ae31-688ade0c4224 | -5.3756 | -46.288898 | 2026-09-10 00:28:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0f12825a-9530-3081-b21c-f17694b5d331 | -9.298 | -44.365799 | 2026-09-10 00:28:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 44b8fa90-cd7a-322d-860b-08bdbe7ef106 | -12.8608 | -44.6161 | 2026-09-10 00:28:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4a9131d1-c1bb-3538-ac42-a46378a6328a | -9.6822 | -43.437801 | 2026-09-10 00:28:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 82a28328-f38c-3ce8-85f5-09362ddf8c0e | 0.2622 | -51.470001 | 2026-09-10 00:28:00 | METOP-C | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 95ccb3fb-4886-38f9-8426-a1b7877f3d42 | -12.8418 | -44.3484 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bb64a41a-7768-36a9-a692-5af892a85f6b | -6.7264 | -44.044201 | 2026-09-10 00:28:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d47c880c-87ce-3b32-81ee-8ab0f6f8e415 | -5.4818 | -45.1325 | 2026-09-10 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7884a2b-25b8-3887-be05-00f8044a511e | -7.2555 | -45.355099 | 2026-09-10 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87797d9c-a347-3a78-b25c-6fc550059222 | -7.9819 | -43.983799 | 2026-09-10 00:28:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f0863573-f750-39dd-8c34-4400e7be8692 | -8.9792 | -45.000301 | 2026-09-10 00:28:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 95cdc02c-0c06-3be3-911e-d2bb3432ecb9 | -9.656 | -40.623001 | 2026-09-10 00:28:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b4e874cd-c733-3467-9b48-fd18d59861a7 | -9.3304 | -45.639099 | 2026-09-10 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7feaf287-a640-3bfa-8e53-3f4e8efe6fc9 | -11.2085 | -46.348999 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b407f914-de6f-36ff-a34c-2a5700522e12 | -2.9342 | -50.465599 | 2026-09-10 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b450ff77-80a1-35af-8829-f607132cd7a2 | -10.5535 | -46.086399 | 2026-09-10 00:28:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a9f4212-81e9-3e83-b361-b7785ca84f9c | -5.6036 | -44.8554 | 2026-09-10 00:28:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f47e861-c906-3dbb-b2d0-b65eec150798 | -7.496 | -45.279099 | 2026-09-10 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e573fae6-0013-3629-9372-63b2b33221c9 | -7.5109 | -45.254002 | 2026-09-10 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ddf79cd9-1eab-3fef-8d2a-1f188ab69f6d | -9.332 | -45.646 | 2026-09-10 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2dd3da9e-1d1f-3e8a-8a98-e2719500d790 | -10.7469 | -45.9384 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d375c8fd-998b-3f80-8476-0eeaf85e1a26 | -5.7725 | -45.096001 | 2026-09-10 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5492e04a-7e8c-3179-bf38-fad7741cee4c | -12.8222 | -44.352901 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7b3aa9af-4c43-3255-9e51-2a25c2dd3607 | -13.4466 | -43.832199 | 2026-09-10 00:28:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f8f99dd8-a909-312c-b264-127deef124f6 | -6.1724 | -44.637299 | 2026-09-10 00:28:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87c7c250-103a-32a5-ae43-eb943426cf8f | -6.5036 | -47.629902 | 2026-09-10 00:28:00 | METOP-C | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dca9d31a-784d-306f-a1d4-5d833db41222 | -14.9122 | -44.671299 | 2026-09-10 00:28:00 | METOP-C | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1783e147-3f04-3c7f-9f18-185a3f3519c5 | -7.5058 | -45.276798 | 2026-09-10 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3dd10a98-fd62-3ec6-9c3a-19b43000dab5 | -7.5042 | -45.269901 | 2026-09-10 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 971fb079-81c0-3439-b585-9c2adc7bcf64 | -5.588 | -45.3703 | 2026-09-10 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 17e0e467-26b5-328c-9702-54e87fa93b56 | -4.1724 | -42.430801 | 2026-09-10 00:28:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7d65ec6e-e24f-389f-8225-f72005dcb9d1 | -6.8239 | -43.045502 | 2026-09-10 00:28:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d7709df1-3cb1-3550-83d8-0150c78b6e6a | -7.1177 | -42.145302 | 2026-09-10 00:28:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fbb89c71-3031-3128-a2c1-99032747c5d9 | 0.2664 | -51.4515 | 2026-09-10 00:28:00 | METOP-C | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 64d2a294-750c-3e94-a78f-752e16cb96de | -6.767 | -44.576099 | 2026-09-10 00:28:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 25a52231-1bfd-32f4-9606-81da39acf6ea | -10.7517 | -45.959702 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0f83ef9e-642d-3eb1-83a6-5e3d60865dc8 | -7.4929 | -45.2654 | 2026-09-10 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f501904b-6aab-3556-9ee0-ae1f0d3bca04 | -10.7567 | -45.936199 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 94aec41f-fd0f-3791-b3ed-2b964de9933b | -12.8469 | -44.325298 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 37feccde-5be7-30e1-9775-dc4dec954088 | -5.7611 | -45.091202 | 2026-09-10 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8456d582-3f94-3065-b080-4c0c1c984b92 | -7.9803 | -43.9767 | 2026-09-10 00:28:00 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d0a57e70-9951-308b-9faf-706ca8b16427 | -7.5125 | -45.260899 | 2026-09-10 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 85e5c8b7-25ab-327f-ba6d-63f3b1cd2858 | -12.8238 | -44.359901 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5202df61-7fa4-30c0-b770-05d13212bf09 | -6.099 | -44.141899 | 2026-09-10 00:28:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ebe42aaf-7149-3780-9c5b-e1c63c6883e5 | -9.4793 | -48.159302 | 2026-09-10 00:28:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a83555b0-a243-3f87-bb33-30379d33b838 | -5.9234 | -44.944801 | 2026-09-10 00:28:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f69a27d1-a5cf-38b8-8105-51e9a77328a4 | -4.1745 | -42.4398 | 2026-09-10 00:28:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b44b7215-234f-3db6-810d-8b7b27c0caba | -10.4634 | -44.952801 | 2026-09-10 00:28:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b44b0d14-516e-36f7-a0b4-9fe702e9d412 | -13.3629 | -41.337101 | 2026-09-10 00:28:00 | METOP-C | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8b89386d-6859-387b-a3a9-c3d1662c7cb2 | -4.857 | -47.4072 | 2026-09-10 00:28:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ec3cabcf-d7b8-34b0-a69b-43634b9192b7 | -10.0641 | -45.466 | 2026-09-10 00:28:00 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0b415c98-10f7-38c1-a34b-951a797bd0eb | 1.0126 | -51.118 | 2026-09-10 00:28:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ac944614-79d2-30ca-841b-d46cf3d1f60c | -3.548 | -48.176498 | 2026-09-10 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d29be5ae-5a35-336d-89d3-980c6f5de2e9 | -15.7884 | -43.5644 | 2026-09-10 00:28:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 337b6068-8171-3ea7-b030-156ac0d20eff | -5.3633 | -49.151699 | 2026-09-10 00:28:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01c9ba8f-9408-3c9f-a28b-8a9ffedd0dd3 | -6.7654 | -44.569 | 2026-09-10 00:28:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| abe9f11a-b5ec-35d1-a9cd-c6b34c7d93ef | -9.3046 | -44.349602 | 2026-09-10 00:28:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c056e9b8-392f-3920-9d78-1b403a64ea30 | -4.3655 | -47.784199 | 2026-09-10 00:28:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc20c7e9-3e99-397a-b933-23ced7e20619 | -5.758 | -45.0774 | 2026-09-10 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0458ada1-8f65-3172-a30d-63ad9813ec9d | -12.8567 | -44.323002 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1b8483ff-b50b-3f9f-bf06-1e4da7e5b61e | -9.3062 | -44.356602 | 2026-09-10 00:28:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 22239c4a-501a-30dc-8536-9a6c0e0ea1fd | -9.6898 | -45.2234 | 2026-09-10 00:28:00 | METOP-C | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 556c6541-3f3d-3316-b6b1-a645aa714d92 | -11.1933 | -42.787998 | 2026-09-10 00:28:00 | METOP-C | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9f9b9f8c-b597-389c-bf40-d2f57f2cb05f | -7.9786 | -43.969501 | 2026-09-10 00:28:00 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 74e9b5dc-806d-398e-a999-c83f04a5ff3d | -12.8696 | -44.334599 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fe2fb80b-2822-3ead-b9f0-89d3272996f5 | -7.0497 | -42.732498 | 2026-09-10 00:28:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 68f46337-9300-3b35-88ab-4f7d73f387b1 | -1.0988 | -48.0583 | 2026-09-10 00:28:00 | METOP-C | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2d859e8-1de6-386d-a5f0-faf1da8dbef9 | -11.8465 | -44.870602 | 2026-09-10 00:28:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7c0bcfb8-bb25-3038-8950-8a5880e4cbe4 | -11.2102 | -46.3563 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9ae8c7df-866f-39a7-ba3d-09350a3bbb1f | -12.6338 | -47.088299 | 2026-09-10 00:28:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 886b100d-cf39-39bd-873e-9cfb8ca1f30c | -7.5027 | -45.2631 | 2026-09-10 00:28:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a81350c-7f36-392d-bcbf-0bb54ffbc4a3 | -6.1642 | -44.646599 | 2026-09-10 00:28:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 829023b1-b417-3b20-b1e3-6af9c8c77ca2 | -6.4474 | -46.1064 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3b51db5-0bfa-3133-b5f5-2589b0227ea5 | -7.044 | -42.708199 | 2026-09-10 00:28:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6dfbccae-bac0-33e2-81fb-823139521169 | -2.7158 | -57.597099 | 2026-09-10 00:28:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ef69f667-ae0a-334c-a07e-2c171724a910 | -10.0673 | -45.4799 | 2026-09-10 00:28:00 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8da50530-8334-3024-98e3-26366b61bf90 | -5.6616 | -44.302799 | 2026-09-10 00:28:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dcb2640c-7f96-3ea8-afa7-8da0fa548784 | -9.6681 | -40.630299 | 2026-09-10 00:28:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2780f8ab-db05-37b1-8f43-cbdaf2ba25fd | -12.8289 | -44.3368 | 2026-09-10 00:28:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 28ec4476-ab1f-3470-ae83-c2ba6204a6bf | -5.3651 | -49.159901 | 2026-09-10 00:28:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6326211f-4796-3dde-a8c4-d4c95c1aeb12 | -9.7788 | -43.453602 | 2026-09-10 00:28:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 91291889-649f-3569-9e33-8843562e2549 | -5.3772 | -46.2957 | 2026-09-10 00:28:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c7319923-5fc6-3be8-88f2-3dc163cb3179 | -9.3273 | -45.625198 | 2026-09-10 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 90814fa3-41cf-309a-ae96-2d3336284bd7 | -10.7485 | -45.945499 | 2026-09-10 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 016a7df7-1e65-31df-ad36-98a493932632 | -6.1726 | -44.6432 | 2026-09-10 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| a76cf615-8bc7-3f17-b064-494e6ac930b3 | -6.5637 | -62.8908 | 2026-09-10 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 66a47f4d-8251-362f-bb83-82e77276fb8d | -13.4453 | -43.8366 | 2026-09-10 00:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |


[Clique aqui para ver as próximas entradas](README8.md)
