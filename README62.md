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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fe526ce-afcb-3a72-95a8-c33f4c849b43 | -9.37117 | -62.36393 | 2026-08-17 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9ef4dcc0-1b2c-3f47-a06e-5331fce75464 | -8.90218 | -60.59234 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c77202a7-2478-3785-aee1-33e95bebffca | -6.65339 | -58.95935 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 07316af1-aad5-332b-a590-a63ec618b6f1 | -6.97674 | -59.0192 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5bd215a-f36b-3cc5-8aed-ab8fbf761171 | -7.53059 | -60.68874 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16724b26-1ca7-339d-8ae3-868efff1490f | -6.98591 | -59.04425 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0db3f23-3bf0-3590-9971-7a525472fc02 | -8.9802 | -60.5274 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 27934d23-5bdd-30d6-a39a-0eeddfd636d5 | -6.64058 | -58.96186 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 653840ed-9de4-359a-b4c6-769dfef895a6 | -9.20616 | -59.67334 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4535bea0-6836-318e-8f23-8433dba48bae | -8.95167 | -60.52331 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 20af0579-0cb4-3bf8-b909-69f7d0d557f4 | -7.61307 | -60.95104 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36549332-e142-3992-b1d2-2425a94de90e | -7.41927 | -60.01545 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cee9ec9c-cb95-32fd-9454-70679badb964 | -8.97645 | -60.52785 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94cf840d-f764-3a70-bb55-9cb81b7fcf72 | -6.63943 | -58.96657 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a27716a6-c453-3065-ae6f-f83ccef4cb04 | -8.73213 | -62.89672 | 2026-08-17 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 668b48ca-40c4-3ecd-98e3-b2b563d4c02c | -6.77244 | -59.75863 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 81955ec6-7eb5-3f38-b0c1-fd6485bbb872 | -6.60818 | -58.97146 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 638e2623-21db-3440-a71c-0a4976bdbed5 | -8.97553 | -60.51874 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 601634a3-c989-3d77-877f-06c1b37cdba8 | -8.9569 | -60.57214 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e811e9e-a493-3759-b797-5cd67f6454f3 | -7.60309 | -70.35809 | 2026-08-17 06:01:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79395660-aa5c-3a5b-b7a9-206480a9a367 | -9.37624 | -62.36469 | 2026-08-17 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a47a2168-7261-3e76-9437-520ea7c9872e | -6.71976 | -58.92892 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a12ee167-ccb5-3c3b-86aa-cca3e12e3f3d | -8.98282 | -60.50762 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 885cf30d-5fa0-3f68-a90c-1bbc5375f7dd | -8.98514 | -60.50483 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 125beeab-5f29-3de2-9f5f-09651a18b1da | -6.68868 | -59.06754 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eea8af76-84c7-3d9d-b6c0-e598faa098d2 | -9.17533 | -59.67389 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f3849019-5c52-30c5-9e04-c6e0164e54d8 | -9.36989 | -62.36318 | 2026-08-17 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee374124-549f-36b0-ae06-2a7e866ddae2 | -9.07995 | -61.40257 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7cf6967-53ad-3cd9-9536-87cbc64ea2ac | -6.78415 | -59.4607 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d7746a5-2eca-37f1-b3cd-9a2bcf65672f | -6.71304 | -58.9326 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a59d14de-9f8f-31df-880a-6915a2d33561 | -6.86884 | -56.41287 | 2026-08-17 06:01:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c6e5b1eb-b073-3e7a-b5e5-c2f067dca7f7 | -6.85671 | -58.98243 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46189718-9e3e-3d12-9e96-10c3ef4616ca | -6.83931 | -58.97011 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e51e8694-6da0-3bc4-91f3-9b12137d3a47 | -6.12554 | -57.73312 | 2026-08-17 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f6549dfd-ef37-3ba0-b2d5-864c9ce01026 | -6.65893 | -58.96457 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8861753c-f9d3-37e6-b539-b6dc817f46f3 | -6.64071 | -58.95733 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e11b1b02-9f6d-38d9-b2ea-84a5611ca60d | -6.62727 | -59.06343 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57bb0a4b-d1b9-3e07-b104-8a6eff61a168 | -6.78123 | -59.46563 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f0399b7a-b5a7-3fa0-b2b6-5067398ec1e9 | -8.89651 | -60.5915 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59cc462f-5cf5-3765-9c41-c1da3268984c | -7.40146 | -60.01648 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3dd425b-36be-340b-86ad-7f22df1a4d16 | -8.9527 | -60.51543 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| abf1d316-5d82-3c94-a264-3f709bdf4282 | -9.35093 | -63.56239 | 2026-08-17 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 688c2020-09f8-30cb-a655-48c3e03c3785 | -6.891 | -59.00626 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6162ef21-e00f-3695-b00e-709fc4d10b9d | -8.96983 | -60.51788 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f03ee60-0a9c-3377-902d-59315ad84964 | -10.07976 | -60.49762 | 2026-08-17 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 434ee2c6-3675-385f-ad60-0e2b38465883 | -7.58908 | -61.20742 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80159869-6642-3975-8f46-2a125363eaca | -8.9737 | -60.50318 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0be697a9-9252-3ac7-bd60-ff6509d759cd | -8.97025 | -60.53098 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2a8d477-7746-3a57-81a2-f5bdf6cf0a04 | -6.62715 | -58.96521 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 62c26083-988a-3d67-a43d-b0ae8888fc71 | -11.06199 | -62.56272 | 2026-08-17 06:01:00 | NOAA-21 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 183c2b35-38af-3174-8c24-b528800ace21 | -6.78354 | -59.46511 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ac08f799-e9a6-38ea-81e7-ca4a20dc9c22 | -7.4569 | -60.00146 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4083da82-cef5-3755-9e06-6064ffc0b9bf | -6.65833 | -58.96911 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4b67209b-ce05-3fc4-b939-405121304555 | -8.41967 | -62.67727 | 2026-08-17 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3570cd17-5580-3126-b280-b6a8d0056e77 | -8.98116 | -60.53669 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e397b661-cad6-31bd-aff0-bf86a9e5b1af | -6.63445 | -58.96109 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 43e2a1ca-c330-3eee-a733-893024f0f5af | -8.96776 | -60.53366 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 050c9020-2ff4-3b81-93cf-25525a952544 | -8.97501 | -60.5227 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 967ef98f-0f4a-3f0d-8a57-666c6b0a95d8 | -8.90269 | -60.58839 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 13b04eb0-1512-3f63-8a3a-da064772aed1 | -8.95535 | -60.58392 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17184aaa-f31e-3790-a491-a3b1b4622dbb | -8.89701 | -60.58755 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3721c324-a49d-3837-b3a2-e9483c5bd33b | -8.96405 | -60.53414 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b682eef5-a9df-389a-843c-afbe52a63871 | -8.95204 | -60.58441 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d441cfe-ff6f-3ebb-9f1f-5508034b1e0b | -6.9798 | -59.04331 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce01c9d8-5017-357e-8276-19026cef6b22 | -7.41874 | -60.01939 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 160a2dab-b8a8-334c-8a68-b0b29d4c9dde | -9.5085 | -68.50076 | 2026-08-17 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe201b71-9bb2-3f3d-97f5-62e752ee0213 | -8.98464 | -60.50885 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 20f3a81c-8e1b-3f11-8431-491e14b3ca61 | -6.65396 | -58.95502 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 91c9329b-6151-3da7-97f0-cb861b3af709 | -6.60023 | -58.97988 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b7f8b649-d412-3100-8511-67b0c3716c1d | -7.87834 | -63.7569 | 2026-08-17 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc6230e4-272c-317f-9708-806f852eee30 | -7.43114 | -60.01849 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b269e27b-768b-3327-a970-674052beb989 | -6.65221 | -58.96824 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 02d9100f-bdf1-3826-b714-82f499008d24 | -8.98124 | -60.5196 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a96dba7-5431-3891-908c-2dd2403296c8 | -10.05204 | -62.45759 | 2026-08-17 06:01:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02fe888d-ae8b-3f67-8bd3-5032c2150147 | -7.88415 | -61.79662 | 2026-08-17 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6ccaa17-c0c0-3d5a-a198-45254e14160c | -6.87509 | -56.42097 | 2026-08-17 06:01:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9ef537c7-64be-3b21-963a-7ad550daabd7 | -6.85058 | -58.98154 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75b2426a-0176-3f10-9f6b-700cae231e53 | -8.98176 | -60.5156 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e59dbfe-4be3-3d57-b980-3cbb90465c78 | -9.17478 | -59.67846 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db1e0381-d041-36a7-8225-715cf3e58d31 | -9.37458 | -62.36698 | 2026-08-17 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12dae59c-79e7-3020-97b5-9ccca4046adf | -8.73066 | -62.90751 | 2026-08-17 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 59719b40-6b55-3981-a7ab-cd8a9424bca6 | -6.78181 | -59.4612 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| acb39d50-9340-3617-92c8-2a1a74cd8c58 | -6.86793 | -56.42007 | 2026-08-17 06:01:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e5f32749-2478-304d-9aef-a69ba5bdf314 | -6.98285 | -59.02016 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c37795c-74cb-3382-977c-d9d77978898a | -6.85853 | -58.96843 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c7fc0944-57de-35c7-9fed-57b122f161b7 | -8.96412 | -60.51705 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90f3ca59-ba53-3dfe-97af-31afc9077390 | -6.98164 | -59.02937 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f041c6fa-0d8d-3572-a4d6-49ea7908d767 | -6.62666 | -59.06806 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c80527b-7119-3ebf-a142-7c2fbf0330fd | -8.95578 | -60.60091 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec158f7a-58a2-3c81-8820-fa20886ae732 | -6.1182 | -57.738 | 2026-08-17 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0b6797c6-f593-32d1-8d25-c9272dcd31ec | -8.9501 | -60.60009 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6417390d-62a3-3bf7-95a5-e600b5ceaa69 | -8.90066 | -60.60427 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| eb457c2c-6765-3937-91da-9400141a65fa | -6.86343 | -58.97878 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec5d60e1-c3da-3924-81c0-6d94750de3b6 | -7.61804 | -60.95533 | 2026-08-17 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3aa8d426-689e-3f9e-bcc9-1272562dc975 | -6.98529 | -59.04892 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38c37363-129d-3deb-80b8-4ed77cf21937 | -6.6204 | -58.96899 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1c64317-cbc2-3bfb-be23-b27707c55656 | -6.62606 | -59.07266 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 801f0bae-2e18-3fbf-9148-d3a383fbb2e0 | -7.38631 | -59.99755 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61290894-6932-3d49-be94-c6a690b317b5 | -8.96204 | -60.53289 | 2026-08-17 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5e885de-cbfb-3bf0-b6ab-2517f6902e72 | -6.62415 | -59.07707 | 2026-08-17 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README63.md)
