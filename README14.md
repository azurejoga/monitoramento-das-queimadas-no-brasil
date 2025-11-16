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
| 710de9b5-1a81-3372-a810-200736fa5254 | -6.67852 | -42.04033 | 2025-11-16 03:17:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 49915206-2532-3773-9027-cad433df226e | -6.56353 | -39.76603 | 2025-11-16 03:17:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b9279337-ddf6-36e0-a0c3-52f124fcc12f | -12.04721 | -43.50675 | 2025-11-16 03:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 15cbb752-4f8a-33e0-8554-2c966ce30451 | -12.04811 | -43.50748 | 2025-11-16 03:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0e03ef76-6aea-3fff-b572-5543cb9c27be | -6.93181 | -39.61757 | 2025-11-16 03:17:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 82f4607f-cad6-3384-a83b-843ebc5cda12 | -6.695 | -40.80587 | 2025-11-16 03:17:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1053ddda-9556-3e10-aa1e-fe4fd10eb364 | -7.05617 | -39.62644 | 2025-11-16 03:17:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| f0826559-275a-3bf7-a2c6-f3e543bad484 | -5.72046 | -41.40364 | 2025-11-16 03:17:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b53effc0-a7d6-329e-a47b-7c13fdf0c861 | -7.04647 | -42.24331 | 2025-11-16 03:17:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| abb0266f-1681-375a-a129-54d4f54718f1 | -13.81808 | -44.45044 | 2025-11-16 03:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dc86517b-dd30-316c-9556-a59eec1d8ab9 | -5.99593 | -41.91901 | 2025-11-16 03:17:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6d39df25-9c01-3f0f-ab75-bc51bb7840d7 | -6.81379 | -39.14313 | 2025-11-16 03:17:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 13b074c4-2bd6-3fba-9936-94cf4ac98ce6 | -7.76318 | -38.94324 | 2025-11-16 03:17:00 | NOAA-21 | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 756dce2b-706e-344d-89cf-dd8bfe711a02 | -6.51186 | -39.52461 | 2025-11-16 03:17:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| db279e79-64e4-3913-9fb6-fc58600be730 | -7.0522 | -42.25084 | 2025-11-16 03:17:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 45db204e-a08e-3731-89df-0899b6dc8d76 | -8.15137 | -35.69144 | 2025-11-16 03:17:00 | NOAA-21 | BEZERROS | PERNAMBUCO | Brasil | 2601904 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 804417ce-d586-3f27-b232-173b6ddfd8ca | -7.19743 | -39.21087 | 2025-11-16 03:17:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0be50a61-231f-38db-81e5-0cec5eef1cb0 | -6.71214 | -42.1258 | 2025-11-16 03:17:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 16ce632e-6de5-39ee-aa77-68cfb4505f09 | -6.68484 | -39.09705 | 2025-11-16 03:17:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ee862b52-0a78-32cb-99d1-b5b6c3daa5bf | -6.70234 | -40.8017 | 2025-11-16 03:17:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a8719a92-6bfe-30e2-aae4-e21cef46f3ed | -6.06303 | -41.54981 | 2025-11-16 03:17:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| caf4eca7-dead-38f6-83a7-6c6613e2f965 | -5.52084 | -40.99962 | 2025-11-16 03:17:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| de90033b-2557-3cbb-b719-63855820ec76 | -3.5374 | -40.65174 | 2025-11-16 03:17:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0099b0b0-48b1-3183-a75c-2b11018660a2 | -7.15301 | -41.75896 | 2025-11-16 03:17:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| daa2cc29-a3db-35a6-aacc-bfd4c302464a | -6.0708 | -41.54518 | 2025-11-16 03:17:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5583004b-821b-361f-aeb0-8b5b30ee308d | -6.67033 | -42.04628 | 2025-11-16 03:17:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 1c41ec8c-2aec-3335-8da4-21353d807ff8 | -6.07401 | -41.54395 | 2025-11-16 03:17:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ba952578-395f-3c74-89e1-87325513cce7 | -7.191 | -39.21376 | 2025-11-16 03:17:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e7c31aff-526a-3542-8d55-de8702ba57de | -6.71095 | -42.1322 | 2025-11-16 03:17:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a3d2c160-6347-37f2-b735-569fc80d9b16 | -5.71655 | -41.40771 | 2025-11-16 03:17:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| dbbcb85e-9dda-3181-ba1d-a77652770ce2 | -5.85315 | -39.42692 | 2025-11-16 03:17:00 | NOAA-21 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 80502637-2e2d-369e-86f7-abe5703b0f52 | -6.01124 | -41.91058 | 2025-11-16 03:17:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d657de1d-9809-3ebf-852b-96829ca76248 | -13.81419 | -42.55179 | 2025-11-16 03:17:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 9c1a2c28-061b-331d-9351-819f5d6751d7 | -3.53643 | -40.65734 | 2025-11-16 03:17:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 109c87f4-2eac-3e81-98b6-3bd779ca04c2 | -13.82112 | -43.19073 | 2025-11-16 03:17:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b7523200-a452-3da1-81e3-ac619884a51e | -7.41281 | -40.06755 | 2025-11-16 03:17:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 48b2351c-3fbd-3198-b1fa-b9573991d988 | -3.58287 | -41.66015 | 2025-11-16 03:17:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 90e127c5-39b2-3360-a57f-601c3343f82c | -7.05539 | -39.63076 | 2025-11-16 03:17:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 9a90e0f5-c4c9-3b10-b845-265a5e7a08cc | -6.71249 | -42.12634 | 2025-11-16 03:17:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| f7da7402-a7a4-3f1c-9b27-0b8a7049fd57 | -5.4794 | -40.96716 | 2025-11-16 03:17:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e976c38d-a04a-3c5c-8425-45e9c408b09d | -5.99839 | -41.90611 | 2025-11-16 03:17:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a47b996e-509a-3004-8f28-fdccbfc0ef61 | -7.40598 | -40.07098 | 2025-11-16 03:17:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 7321a5f3-6219-3963-8095-5c5e7ce24e9b | -11.41863 | -43.33096 | 2025-11-16 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8c426690-6d4e-36ea-a2a3-3c34195bd4f0 | -3.85265 | -40.76117 | 2025-11-16 03:17:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| ec87c043-3cad-3e55-a0e5-165912a11f06 | -7.75762 | -38.94221 | 2025-11-16 03:17:00 | NOAA-21 | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 72fe5587-ca29-385e-b0d6-6ace648f1566 | -6.81945 | -39.1445 | 2025-11-16 03:17:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 08b6af2e-d698-3581-8cba-fe023849de8d | -5.53176 | -41.77126 | 2025-11-16 03:17:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 95736848-ac76-34c9-9251-d9a3465a2653 | -7.05033 | -39.62518 | 2025-11-16 03:17:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 6903f05e-0053-31b3-90af-68c490314589 | -5.99514 | -41.9211 | 2025-11-16 03:17:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d6dda9f5-3fde-3b22-a929-664ed4136f06 | -13.39062 | -40.65652 | 2025-11-16 03:17:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 16984ebb-a49f-3b64-986b-d42197608aef | -12.04589 | -43.51318 | 2025-11-16 03:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5b5397d0-fd98-3799-b88f-1c91859d8e43 | -7.0523 | -42.25026 | 2025-11-16 03:17:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b6da8ed9-6b71-36fb-ae18-1bc21d2c3dce | -14.20424 | -41.84762 | 2025-11-16 03:17:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1e97540a-cc6b-3e1e-b05c-76e06ca2eb4c | -6.67427 | -40.80012 | 2025-11-16 03:17:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a7316df7-cb3e-3fda-8899-c0682b1b4c08 | -5.52179 | -40.99427 | 2025-11-16 03:17:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 15f3d01e-58e7-3d14-b3f5-b2917213c44f | -3.59685 | -41.66278 | 2025-11-16 03:17:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a14fae3d-8b2d-3d75-ad48-7e88dcddef04 | -11.41182 | -43.32954 | 2025-11-16 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a571130e-a936-399b-a60a-807c81bbd7d1 | -7.04525 | -42.24994 | 2025-11-16 03:17:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 9528c331-f632-347b-bb1f-489e336bf184 | -6.3674 | -39.62695 | 2025-11-16 03:17:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0dc73287-dd32-3b04-bfee-5596fe88c740 | -7.40681 | -40.06643 | 2025-11-16 03:17:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 9.4 |
| e816c634-2933-3c73-b54d-9290f5d49c4a | -15.38028 | -39.30965 | 2025-11-16 03:19:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 915bb720-78e6-34d1-b2ea-24efefbe1fc9 | -8.06657 | -43.10132 | 2025-11-16 03:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 26ed3e46-96c5-313d-bc07-a92a0166218b | -9.50484 | -35.58732 | 2025-11-16 03:19:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6a3ffe9a-222f-3290-a32f-90172bdfea5a | -9.10792 | -40.46231 | 2025-11-16 03:19:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2a447c73-4be5-3f4f-a788-5bdd8c841165 | -8.06099 | -43.11094 | 2025-11-16 03:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| e9926362-4a0a-3e93-a2ed-7697b3adab08 | -10.14913 | -36.35711 | 2025-11-16 03:19:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 8b68b8e4-da53-303b-abb7-28fa4483c51b | -8.67524 | -41.03099 | 2025-11-16 03:19:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dec31634-515c-3dae-89e2-bd38e54ed4e9 | -16.13933 | -43.6607 | 2025-11-16 03:19:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a1b56e9-4c1c-3a56-a2d8-c1293b40a7f6 | -8.05947 | -43.09995 | 2025-11-16 03:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 45.4 |
| 76103246-1154-32df-9df3-78c0f030154a | -18.69736 | -40.11069 | 2025-11-16 03:19:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3366206b-f305-39ed-8695-961592cf8fad | -17.02965 | -41.45037 | 2025-11-16 03:19:00 | NOAA-21 | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d03713f9-65a2-3fc9-a008-f2004ecd5623 | -18.69858 | -40.10484 | 2025-11-16 03:19:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9ec1dbbf-3fc9-3302-97e9-46810e9547e8 | -9.11392 | -40.46336 | 2025-11-16 03:19:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| aee4351e-e5ee-337a-845a-c4330fa75535 | -8.67429 | -41.0359 | 2025-11-16 03:19:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e769539c-b1a9-3da3-ab8b-480299ac710e | -9.69578 | -37.77862 | 2025-11-16 03:19:00 | NOAA-21 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6a61cad9-999f-30a0-9f61-8b0ece178afe | -9.11478 | -40.45887 | 2025-11-16 03:19:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 161a3e76-f42e-3acd-827e-0b8498637e9a | -8.06238 | -43.1039 | 2025-11-16 03:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 79cdd8b5-2a1b-3fda-b595-6f9aff3e49dd | -18.70131 | -40.11 | 2025-11-16 03:19:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 47113a5f-bc06-3021-b800-4b6662f4c934 | -15.46118 | -39.23967 | 2025-11-16 03:19:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 548da6b0-7a9d-386b-b62a-f9e8b011d1ad | -17.03032 | -41.4472 | 2025-11-16 03:19:00 | NOAA-21 | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4a40b4aa-a184-30e3-89aa-1ba7688ba5c4 | -8.05662 | -43.09578 | 2025-11-16 03:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| b11db097-01ad-390a-ab59-fd8667b5a036 | -8.06524 | -43.1083 | 2025-11-16 03:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 0917d722-17dd-3cf4-b7fe-b37efc240952 | -8.06375 | -43.09697 | 2025-11-16 03:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 008f49f4-467e-3b13-a954-38a42a2aae72 | -8.05814 | -43.10691 | 2025-11-16 03:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.2 |
| eb2610a2-f97e-3986-9eab-a12ec962967f | -16.14054 | -43.65523 | 2025-11-16 03:19:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f994bd5-fc8c-38bc-9162-1e1901e879ff | -15.38011 | -39.30971 | 2025-11-16 03:19:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 02d2efda-a946-350c-92e8-5794f418088e | -10.14994 | -36.35248 | 2025-11-16 03:19:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1b13e497-d28d-34f1-91f3-a24df78c40a5 | -9.10879 | -40.45782 | 2025-11-16 03:19:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.3 |
| de4df60b-b06c-34bd-ac46-56957c9887ac | -8.05526 | -43.1026 | 2025-11-16 03:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 2f6cd01c-97f0-36f0-a9c3-f601f8572b81 | -2.5238 | -47.8332 | 2025-11-16 03:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 9cf56866-254f-38a0-8883-27b4666b1689 | -12.0 | -49.2901 | 2025-11-16 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 7c1b8981-b052-3ae8-8758-2abc9ae4498b | -4.4246 | -43.4038 | 2025-11-16 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 3f7fdb1a-272e-3f35-b83f-952ea99cd932 | -2.5238 | -47.8115 | 2025-11-16 03:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| da146cbe-c75a-313b-89db-b07eec202e9e | -2.5053 | -47.812 | 2025-11-16 03:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| c2093763-f9cc-399a-9c95-302cf4f5ec78 | -12.0004 | -49.2683 | 2025-11-16 03:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| d81634ec-7afa-3de2-b1a4-301ec50c0def | -12.0004 | -49.2683 | 2025-11-16 03:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 5353d593-3561-30bd-a258-f5a943d1d13b | -12.0 | -49.2901 | 2025-11-16 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| ff629a42-67d7-3cc3-bee3-a87d0669eacd | -2.5238 | -47.8115 | 2025-11-16 03:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| b2aabcd9-b9f0-369f-89bb-82fa62157ccf | -4.4433 | -43.4027 | 2025-11-16 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 1b3684ad-f042-309f-8401-f1cd3e1e87a2 | -4.4246 | -43.4038 | 2025-11-16 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |


[Clique aqui para ver as próximas entradas](README15.md)
