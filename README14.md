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
| e20aa393-b15d-30f1-be90-986840640e1e | -6.33295 | -41.59629 | 2025-10-14 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e6daa533-0557-38a2-89c3-46f62e7a91dc | -5.74562 | -44.51237 | 2025-10-14 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77d2956c-3e04-3fd3-9a9c-2246959746e6 | -5.01712 | -46.76842 | 2025-10-14 04:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5ab65b9c-6368-3778-8af1-2d7564615c97 | -7.74701 | -42.44396 | 2025-10-14 04:04:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cc4e942c-9d8d-376c-a1e8-a92cbbd10b13 | -4.04979 | -47.25662 | 2025-10-14 04:04:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 153b6190-4747-3d93-b180-3ab510cb163d | -7.16767 | -42.19686 | 2025-10-14 04:04:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5d127271-8cb2-35d1-bb57-205b40baea4a | -4.55637 | -49.64827 | 2025-10-14 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c08e963c-3ee7-346e-a3c8-2f1506c5a832 | -8.23551 | -43.34163 | 2025-10-14 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8924de5e-db9b-3e84-bcd7-b0227362cc74 | -6.53422 | -43.55959 | 2025-10-14 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a838438a-7f75-31e1-b7d4-712878f318d4 | -7.20352 | -45.48249 | 2025-10-14 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7b5ce85e-e797-3ea7-95ca-7da345e0500d | -2.6889 | -49.06723 | 2025-10-14 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53226f25-e1c0-3fc0-93c2-06aef088eb18 | -6.33028 | -44.01395 | 2025-10-14 04:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eec7c654-370b-356f-b5bf-75e37278528b | -4.28503 | -48.576 | 2025-10-14 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 296ad787-8a05-3eb5-ad2b-2873e8e93db2 | -6.32291 | -43.90118 | 2025-10-14 04:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09b44183-cf10-30de-9712-83c5b22a7fb0 | -6.28732 | -43.90491 | 2025-10-14 04:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1b224bd-686f-3f89-a346-a2607960cdc2 | -5.11754 | -45.49867 | 2025-10-14 04:04:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6b39f81-5071-3606-a67e-6123e9ace4ae | -5.49041 | -44.99798 | 2025-10-14 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ac10612a-d60f-3ead-a158-642fe8b61580 | -5.69911 | -49.30447 | 2025-10-14 04:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ae6232a-c607-3b43-b595-14c413648d37 | -6.02639 | -43.40343 | 2025-10-14 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92af53c4-1440-3efe-82a4-ecb597f365e3 | -7.42254 | -45.41772 | 2025-10-14 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4711b207-72a2-3bb2-a808-4cc3c754c2d0 | -7.75435 | -44.19395 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98a075d3-5273-3597-b592-f00e8441a5c8 | -5.73665 | -47.47612 | 2025-10-14 04:04:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe81abab-26b1-3907-95d9-81312b1b4a61 | -7.45305 | -38.97377 | 2025-10-14 04:04:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 71124448-65bb-30f5-8c9c-068e84462a73 | -7.92893 | -44.11816 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 293a1842-e413-388b-a1b2-eab1c0f407d0 | -7.75509 | -44.73646 | 2025-10-14 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ba171ebc-4d56-3618-a71c-b9e99d8ad798 | -6.5673 | -43.91838 | 2025-10-14 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a4dd9e60-2af9-3acc-a8e4-1fde49a0bc24 | -6.5114 | -43.99894 | 2025-10-14 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| be9ceb13-613b-3534-9025-b00ddc53a942 | -5.88472 | -42.90577 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9904123c-0487-379f-93ef-2247114632f0 | -4.83934 | -42.77002 | 2025-10-14 04:04:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 003381db-0017-393c-89d6-e70a863d73f0 | -4.65997 | -43.13656 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 9fefaa6a-b7e5-3b78-9dd1-aff52ace9107 | -3.1335 | -50.21126 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b6bc54a4-20cc-3ad5-af8d-f9907402ef9d | -5.62563 | -42.68642 | 2025-10-14 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f134489a-818b-39c1-acf3-0174da017145 | -4.73973 | -45.6515 | 2025-10-14 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 458e2db2-954c-388c-ad21-288571ddb2be | -5.73553 | -51.30902 | 2025-10-14 04:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fafe2fe8-869e-32bd-a78a-01b2a593b6e4 | -7.93642 | -44.11943 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 332ac3db-7c31-312e-b180-9f8243aaa7ff | -5.6214 | -42.68986 | 2025-10-14 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 70604813-8fee-3a30-9b8b-5af79fd371c8 | -4.73905 | -45.65565 | 2025-10-14 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7131281d-395b-378e-a432-f618aba1d7fb | -3.09833 | -51.2944 | 2025-10-14 04:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5ef6527-a717-3e32-84ec-5482c56a076e | -5.61968 | -42.72296 | 2025-10-14 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ede94a67-e9d7-374c-95f2-8a54df4f59e1 | -5.30907 | -42.90955 | 2025-10-14 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8df2730-7d35-37a9-9d52-b8a94dd70e5f | -5.88695 | -42.91467 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ae3cef03-362d-34ce-9309-d8b65ca262c9 | -7.91921 | -44.13042 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bd7a2d42-d7aa-35e8-b502-f7c4457d98a2 | -3.12822 | -50.20593 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a8a3507-52d2-3515-afe7-320691d18c9f | -4.80376 | -45.34092 | 2025-10-14 04:04:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 01067a82-8b79-3004-a745-e23c832843c3 | -5.91042 | -42.81695 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f9d67ec5-5020-36af-980f-18c415a741d2 | -5.86923 | -42.88286 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4f6600c7-b7e5-3c56-9a13-43b48adb6a9c | -7.75285 | -44.72606 | 2025-10-14 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3ee1986-6ec7-3cd1-a6d8-0b4a2c8b498f | -5.73944 | -40.7666 | 2025-10-14 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7d367d68-b5e3-3225-b7e6-337775bc22b2 | -6.57538 | -43.9128 | 2025-10-14 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4bcd5cb9-d61e-3c6a-bcec-b1e3f8de4ca6 | -7.75898 | -44.73711 | 2025-10-14 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cd258f26-bdd3-3948-ba88-34d1385146a0 | -3.13208 | -50.21461 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 93de7622-393e-3d38-ab8e-6bfc57778ae1 | -5.1755 | -42.90675 | 2025-10-14 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9bc6b5f-5da5-35b4-b183-faf22f9310aa | -5.3127 | -42.9101 | 2025-10-14 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8c1f096a-088a-3c2f-9e4d-5c7fa8c0970d | -6.44478 | -41.83725 | 2025-10-14 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e8762ea5-b5db-3ea8-963f-92f4eba4a48d | -6.44742 | -43.99031 | 2025-10-14 04:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 96e989dd-865b-3c91-93d0-369259f5e53a | -6.44538 | -41.83355 | 2025-10-14 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 76cd8ca9-79e1-3c58-a8c7-53e7c9eb6002 | -4.83957 | -41.63201 | 2025-10-14 04:04:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0c4de848-4cf9-3a35-98d2-510f42359b32 | -7.54357 | -42.67675 | 2025-10-14 04:04:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 206f3c1e-95c4-3213-b777-c517761a1015 | -4.23741 | -48.69133 | 2025-10-14 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f26d5532-1d86-3df1-9ece-e8bb061b9a48 | -7.82316 | -46.92662 | 2025-10-14 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e0c82ac-fb2b-30ae-b3df-4b53e85949b9 | -7.29087 | -41.95992 | 2025-10-14 04:04:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 14c83b11-6c27-37e7-86de-c6efc196631f | -6.44418 | -41.84097 | 2025-10-14 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 706d4767-b613-3d5c-8d09-604768b9b16e | -4.66665 | -43.14216 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 832a71e9-37dc-3762-935a-30a9f25cb6f8 | -5.49168 | -45.40696 | 2025-10-14 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d6f84004-f66f-3e08-9313-9a7b9accf479 | -5.91399 | -42.8176 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4c3acc84-98ed-3615-90c3-12bab383bd09 | -8.53483 | -44.585 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bca45a44-4785-3d0d-a5e2-21c0b37c3b0d | -5.47323 | -43.38531 | 2025-10-14 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b215f5d-dbc5-382a-88bf-8172aacc308b | -3.70449 | -43.21309 | 2025-10-14 04:04:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dba68db2-efba-3da0-a15f-241b90829e2c | -5.97695 | -43.56298 | 2025-10-14 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ff010fc-6d1f-3c9c-b995-37892212f7dc | -6.42021 | -42.43726 | 2025-10-14 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 057c26ca-365a-3668-898c-baecc590e8e2 | -2.69229 | -49.06939 | 2025-10-14 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ed47616-adad-3f8d-b20c-3f7cbda7fa07 | -3.12675 | -50.20929 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7a249b7b-9771-35f3-9f41-3b0f80254853 | -4.59788 | -46.34272 | 2025-10-14 04:04:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2c7ec86b-43e1-33a0-aa7c-940f60b8d0d7 | -3.13134 | -50.21903 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 50c4982a-e264-35f0-897c-4edc6afb3099 | -5.89919 | -42.84039 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c37f6b76-0485-3268-a1d3-ede56c8a8e1e | -6.02709 | -43.39921 | 2025-10-14 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0450a5e-8e36-375b-88e1-6baf7b8f9b0a | -3.43244 | -50.2552 | 2025-10-14 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e58f6385-1b65-3f7b-9c82-847f941ddf75 | -7.19947 | -39.35678 | 2025-10-14 04:04:00 | NPP-375D | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 43f004e9-7efc-3682-bfb5-90783bf31ff3 | -6.56658 | -43.9228 | 2025-10-14 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3828fada-efc7-3c97-b008-c5b1e472f758 | -4.62528 | -45.77372 | 2025-10-14 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46ce4b8f-d259-3e05-bfe9-8a1f85676280 | -6.18576 | -41.75102 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cae31c62-cb92-3388-b93c-db97fa735a25 | -4.05558 | -47.25197 | 2025-10-14 04:04:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5f979ec-f44a-3a74-867c-db140482691d | -6.15469 | -41.77304 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 032946a8-6275-3c7a-b8c1-a395d61d3005 | -4.6235 | -45.78328 | 2025-10-14 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08929342-c57c-30d5-a4a0-d0ae4d50d32b | -5.9762 | -43.56747 | 2025-10-14 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b7741b6-60f2-302b-8187-b747ca4e81c7 | -6.44657 | -41.8261 | 2025-10-14 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cc6269e0-e3ba-3e13-8f3c-830c77e42a56 | -3.09673 | -50.38695 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d1f318d6-6d8a-3df8-a76f-597d6f004e8d | -7.08217 | -43.70041 | 2025-10-14 04:04:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d8c02966-813e-3909-b79b-d02504311c88 | -3.50969 | -49.72332 | 2025-10-14 04:04:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4f15c34-7bac-31c7-bcb8-4b0d285c47f5 | -2.69291 | -49.06554 | 2025-10-14 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 756c61bb-4857-307a-b5f6-5f7756c72f55 | -4.84017 | -41.62827 | 2025-10-14 04:04:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 64c89c3c-b29e-3e12-9129-4b652d159eb1 | -6.14559 | -41.7639 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 991e59f5-aa22-3fe5-9aa7-9ec397bf111b | -7.24217 | -46.25781 | 2025-10-14 04:04:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7f90d0d-1856-3f17-8ed9-7db7dd3b791e | -7.92967 | -44.11367 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9701d1d4-408f-3c75-be72-a677d84bcbf2 | -5.74434 | -47.47105 | 2025-10-14 04:04:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ea507d9-6948-342c-b688-3bc5c33d49bd | -5.49991 | -43.06775 | 2025-10-14 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| acd19551-70c6-32c8-b88e-abf3a962560d | -3.27477 | -50.04966 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73294a69-9f13-3479-858e-5d0a635b94c2 | -3.04512 | -40.1154 | 2025-10-14 04:04:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 0ff928f7-e734-3eaf-af51-0386026cf7ff | -0.89723 | -47.54808 | 2025-10-14 04:04:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d49afe99-7261-3201-b6d3-a166672c9748 | -7.75573 | -45.71576 | 2025-10-14 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README15.md)
