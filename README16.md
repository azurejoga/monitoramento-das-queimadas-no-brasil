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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a327c517-fc01-34f9-8fa6-52a4165fc1e6 | -6.63896 | -44.63801 | 2025-08-07 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72c950f1-e3da-3c19-bad7-708710bb1c6c | -7.9129 | -45.53791 | 2025-08-07 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50cea6d6-f135-34b6-9aa5-dae11b1808c5 | -9.08454 | -45.0649 | 2025-08-07 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6c5f9a6-83bc-3173-8d71-eba6eecbca15 | -3.64959 | -48.32304 | 2025-08-07 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cbe7c4a-8713-3c57-8cc6-415c182ee3c4 | -8.92277 | -60.59757 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3f9197a-de06-3ef7-b67e-db9382198eb0 | -10.43261 | -44.40355 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1de85586-753c-342e-bcfc-a6025afdef53 | -9.74468 | -48.57412 | 2025-08-07 04:51:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cfd33df0-ca00-34a4-8cb7-5b882eb56885 | -7.36863 | -44.15537 | 2025-08-07 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f874e6de-9a8d-3117-8ed4-cdcddb143ca6 | -10.62744 | -44.76789 | 2025-08-07 04:51:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 41506208-fcdc-39b8-883f-2eb6f80bdc41 | -6.41662 | -53.37067 | 2025-08-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 249eaf2b-5bf6-3449-b141-bbf768063608 | -8.91498 | -60.56112 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0c1253b-ec0c-3088-8c98-dbc4fe92aea5 | -8.92224 | -60.55389 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36481a6d-24ce-3df0-9cbe-b393ca1a543c | -7.03114 | -42.54716 | 2025-08-07 04:51:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f5248a57-2e72-3915-a8ea-7bbe1a39bbeb | -10.47226 | -44.39255 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b46bca1-340a-3ae8-946a-08b822f67c44 | -8.91146 | -60.58062 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9c92a23-2ae1-3ac0-99bd-3e414ee38378 | -8.52227 | -43.29588 | 2025-08-07 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b1fb16f9-0989-3925-9cce-52a06fbb2a27 | -8.91297 | -60.55228 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55f4c1da-23ff-3c90-9186-2985d2b1f342 | -6.64005 | -58.82647 | 2025-08-07 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6583c5d3-8302-390b-9f66-3529b2d9b2aa | -8.91387 | -60.54086 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 423266cf-504f-332f-9666-8b06d8b1f9a9 | -8.90666 | -60.56118 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 173cffa7-1d99-3628-8144-469a9291a4c7 | -8.90393 | -60.56937 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 673e65ec-d2e0-3451-b8b9-090cdd6b1157 | -6.6638 | -51.95998 | 2025-08-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 687dba60-c45d-31c5-9fa4-0a9124317bef | -6.92072 | -52.84402 | 2025-08-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 75eaa196-1178-3ee6-9209-3304b971a567 | -7.03048 | -42.54971 | 2025-08-07 04:51:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 41e9d10f-03a8-38ea-ae20-55f1d6c586f6 | -8.91593 | -60.56279 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a6ff39a-a65d-3e4b-8785-03793182e65e | -5.72514 | -49.09957 | 2025-08-07 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8a1fd93f-0cf0-3589-a2b8-801381e4598c | -7.36298 | -44.15771 | 2025-08-07 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3f55127-e40c-363d-80a6-58d83df48f04 | -10.42314 | -44.39183 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90c4d77b-7bc8-39a4-a834-d485ed4a8925 | -8.91321 | -60.57095 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7bc4724-b916-3b7c-a236-3f3b5fdf2707 | -8.92512 | -60.55787 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0bb3d1c3-e3c2-30ad-84f7-6b0effb1b256 | -6.91411 | -52.84299 | 2025-08-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e2d8f55-3205-3180-b8e0-24299592cc60 | -8.9121 | -60.55062 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5cba4ea3-5d43-382a-a984-87e33ec6e119 | -8.92161 | -60.57743 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 325cca68-3d86-380a-91b8-cdfe86171061 | -5.72882 | -49.10015 | 2025-08-07 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3387c861-3775-3862-9135-0f96e6f765bb | -8.30811 | -55.11033 | 2025-08-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2611a4e9-17eb-311b-99e1-0714607656cf | -8.9224 | -60.76126 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 208ee62f-6bb2-375c-9231-fc4e2b3a4588 | -2.8994 | -54.15323 | 2025-08-07 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6724e79b-450e-3096-aa97-0be75f1301df | -10.47925 | -44.38069 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23435048-7c95-3d3b-8b47-28eaaec6577b | -10.48423 | -44.38447 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 87340945-1f1c-3ba9-b3eb-437526decaf8 | -7.14776 | -44.08555 | 2025-08-07 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4ac8cc9-ca91-3b6f-ad1a-134690e2ba88 | -7.39917 | -60.00696 | 2025-08-07 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 7c0c8588-95df-33c0-a7bb-02553eda649d | -10.7089 | -48.86719 | 2025-08-07 04:51:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 063ec539-e2b1-3149-bae9-603e81addf1b | -7.75871 | -43.59538 | 2025-08-07 04:51:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd15740e-3308-3e97-82e0-27e75eed51f7 | -8.97627 | -40.62445 | 2025-08-07 04:51:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7b4eec02-3e15-3e2d-9d1c-32e45fed9c0b | -3.84367 | -47.75541 | 2025-08-07 04:51:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1bb2a275-b5d4-3f34-802c-97f5fd10ef61 | -8.9161 | -60.58145 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9caacec6-fe59-3454-850c-50b4149ab594 | -8.91873 | -60.56682 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9d71509-6a1a-33c8-97a4-eb954631a573 | -5.72817 | -49.1045 | 2025-08-07 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2866eeff-83f0-32aa-a270-56e0f111dd0c | -4.77575 | -45.32776 | 2025-08-07 04:51:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bba59105-7d3d-3528-8668-c03e4137c70a | -7.3634 | -44.1546 | 2025-08-07 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e10acdbc-45dc-345d-a23f-d7aca1fde9ac | -9.65436 | -43.84457 | 2025-08-07 04:51:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6310fa8f-eabb-3f5a-a808-8a8c966d1c30 | -5.87706 | -57.74912 | 2025-08-07 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0801df90-6b22-3372-9171-2f40b8bf586a | -6.85885 | -44.30895 | 2025-08-07 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 58e1ebd2-8daf-34c3-9f68-d44d3cd5ed84 | -7.19244 | -45.48257 | 2025-08-07 04:51:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f843236f-f44b-3556-be56-e75f6a3189de | -6.15358 | -55.80839 | 2025-08-07 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d721765-0e57-3e6f-ac65-62f194f280d3 | -8.91962 | -60.56193 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9ec745f-edce-3986-9e16-b6ddeff6aff0 | -8.90682 | -60.57981 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0e7d72e-d0c7-3a80-a5d7-76b5042d2594 | -6.52866 | -45.57864 | 2025-08-07 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5b326d8-0220-3e7f-a584-b8ee83cbfed0 | -8.90507 | -60.58951 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 873a6b8c-2789-36fb-8d81-c8e9478ce554 | -8.91173 | -60.6057 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0496b22e-95cc-3145-b05c-1a601594308d | -7.40293 | -60.01242 | 2025-08-07 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 4bdceeff-02f0-351c-9352-660e3f8066c9 | -9.08029 | -45.05824 | 2025-08-07 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc1b5240-1c90-30c4-b915-c8c21ead609d | -8.91255 | -60.58235 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f37f98fe-d117-3477-8b80-56fc80dbf718 | -8.92508 | -60.74621 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 1754af11-f1b8-3e30-bce9-526375fd095f | -6.94849 | -51.63452 | 2025-08-07 04:51:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ce3300d-87b0-356d-b9e7-e4e0d775255d | -5.87589 | -57.75618 | 2025-08-07 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c101cecd-9296-364c-8a0d-9eaa0d4eb844 | -9.46784 | -57.85151 | 2025-08-07 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 33809017-ab84-3de6-b669-ee4991f330e6 | -7.19215 | -59.83795 | 2025-08-07 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3878bad-65db-3720-8b67-2d8842b0ad63 | -8.24543 | -45.0741 | 2025-08-07 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ac0c6a7-3e7b-3751-9e84-20adabe08612 | -9.08573 | -45.05593 | 2025-08-07 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 876595ee-cb5a-397a-83fc-e0a33e21f527 | -8.90482 | -60.56444 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37a4e27b-2216-3f25-9f63-7070f39f08b3 | -7.59887 | -55.19741 | 2025-08-07 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d078afa7-365b-330f-8e12-36a3db13c627 | -8.90371 | -60.55064 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 03f57e8d-5b61-3c92-a480-e2ad75ca2ed7 | -10.70443 | -48.87007 | 2025-08-07 04:51:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e480c318-3d73-336c-9868-458e23e4ccbe | -8.90494 | -60.57108 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10e521fa-b998-3884-8178-8aeae53e6647 | -7.41211 | -60.01385 | 2025-08-07 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ec1403c6-86ee-31d7-af47-dee39fef5725 | -8.91522 | -60.5863 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3ae9ca5-d3d9-3aa5-a26a-9057815d0f39 | -7.39834 | -60.01168 | 2025-08-07 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e172532a-b44e-365f-8f42-7b68cc5b487d | -4.31347 | -48.07928 | 2025-08-07 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| edaed08e-be66-3f44-86ac-d6b0ab5ba81c | -6.42103 | -53.36424 | 2025-08-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1c64a1d-9905-3853-a499-a1373799edb8 | -4.0011 | -47.09229 | 2025-08-07 04:51:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9b636d3a-7e7a-3b04-84cd-98af23cc8e1c | -10.4343 | -44.39003 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4bc01cd6-e04d-37a7-9818-42c7fcf1a605 | -10.42767 | -44.39935 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6e6ca64-e60e-36b1-b752-ff133a1db36a | -6.64433 | -58.82718 | 2025-08-07 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dab63bb0-bb4c-30a8-a174-c1671ba12cf0 | -10.42231 | -44.39857 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f16c9d7-eef9-3002-9a81-b30e8dfbaed6 | -8.5208 | -43.30747 | 2025-08-07 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d5b1a324-991e-3086-94ef-04ed27400edc | -8.9186 | -60.7554 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 557f6f4f-89cd-3831-b914-9c1c8173172e | -8.51721 | -43.30587 | 2025-08-07 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b75bb7b2-a9bb-3604-a4f2-600985cb8a5a | -8.91849 | -60.54168 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f065ed0c-cb9d-33f3-a917-ce1905426d16 | -5.7325 | -49.10073 | 2025-08-07 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c11c124-cd6e-3469-bf16-f36b7a7875fa | -10.44543 | -44.38847 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4eea67df-1d98-3ad5-b60f-ed4e7eb24118 | -8.91726 | -60.6016 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9a0f6a9-4c16-3cbd-b563-3012a959ea0e | -8.92128 | -60.74036 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| d773dd5b-2628-31e6-917f-a597f95f6130 | -10.44459 | -44.35156 | 2025-08-07 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f871d5f-42fa-32b7-b590-95f12a4979f8 | -6.81559 | -42.9957 | 2025-08-07 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 067e4b7f-77d4-3f47-ae97-7f28bb231e0f | -9.01464 | -51.11803 | 2025-08-07 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31c294a1-25fc-3405-91fa-f44695bf010f | -8.91058 | -60.58549 | 2025-08-07 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a96c2832-bb2e-357e-81f3-d1664a45c7fe | -7.14859 | -44.07936 | 2025-08-07 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d12cbce2-60d4-368e-b63a-1f9360f74b22 | -6.15717 | -55.80898 | 2025-08-07 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ecd67e4-b2ec-3813-b8c0-01498816c7a1 | -7.23755 | -44.63447 | 2025-08-07 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README17.md)
