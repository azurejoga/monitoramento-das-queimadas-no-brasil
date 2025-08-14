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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3726aa7-8d3a-3010-94e3-86eca7d3043e | -8.52073 | -43.32349 | 2025-08-14 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 135dc815-d18c-3ece-89bb-8a178729c407 | -6.77751 | -59.4733 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa84992e-446c-36b5-9d40-31d4314347ad | -6.10646 | -59.91872 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0059852-15ac-354c-9dac-23adc77637cd | -7.07159 | -59.20694 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0677da31-1417-3e83-ae97-05d34f29b154 | -6.08993 | -59.9503 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7f2c05d3-29d5-35fc-97c2-f7e03294b1f0 | -5.74829 | -59.88785 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d533d65c-6fa7-34ac-a7a0-64cd20631b84 | -5.73703 | -59.88948 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92f6983a-a0bc-390c-8a59-2394808ab6ea | -5.75455 | -59.89867 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c32a124-58c2-3820-a26b-5b0ed305b190 | -6.09286 | -59.93369 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59ecb4e2-ddc2-3ad5-a467-14be859abd37 | -6.88903 | -59.13781 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21032a9f-90da-3f7d-a467-4a6ff688e1e5 | -5.7361 | -59.87868 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e9ba33f-d951-3646-bc9e-d1994f532492 | -7.14098 | -59.65862 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ba6e3f5c-fa6c-3daf-aa4a-664487599f65 | -5.75573 | -59.89201 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fe73081-d594-3f1b-b3c1-ecf8a0228a2c | -5.73929 | -59.87619 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f0e27f5-f6bc-331b-9a73-c8fee928b3b8 | -6.10297 | -59.93858 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 744c1b49-c077-3a69-8464-90368ceab5ad | -6.89602 | -59.1272 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fdd3dda9-cd64-3ba9-862e-4d80d4fadb23 | -6.08694 | -59.93616 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e2e0190-e0dc-3938-ac99-e58352c84a69 | -6.0752 | -59.94045 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b39b54f-84ff-35bb-aa6d-f5cd2bab18fc | -6.88658 | -59.883 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef46e3d2-fa6f-3f20-82c8-8f002e6bec0d | -5.74716 | -59.8945 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34bad4b4-e175-32a1-a1fa-946e86a18c9e | -6.87014 | -59.15767 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f7056ced-087b-3eb7-b86f-bb488da3b36e | -7.32657 | -60.62569 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eaebcb27-dc62-33c2-bdfe-4362b53faa1c | -8.80355 | -52.04148 | 2025-08-14 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de6ad653-86c2-3c22-b936-c75c1e63d699 | -6.53934 | -56.19625 | 2025-08-14 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67695d03-3901-33d8-a121-bb70b3b2f97f | -6.89006 | -59.16123 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 5e9d67bc-ca4b-36cc-bc45-47ad0c4cc75c | -6.77508 | -59.47171 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad6ea664-0586-3816-872b-43feaa451292 | -6.08578 | -59.94274 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 35d9bb3c-c1fe-30ac-90cb-f0fd3f3b6c8d | -5.73909 | -59.89273 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5412adf-2b11-3607-9eab-4fbea4636059 | -6.08636 | -59.93945 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9825e3b8-3782-3761-8d2d-57d6ff89170d | -6.09762 | -59.93783 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e27a5a2-2cbf-378f-b654-322b58233e5e | -6.90992 | -59.13565 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c455228a-f689-3fbd-88f5-9c868a8527c5 | -6.91791 | -59.14871 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 11b6ba9f-30b0-3a55-bad7-b5a1f3a22b04 | -6.66162 | -59.08925 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5f54558-4f9e-334b-b421-db0e0f46eee1 | -6.89898 | -59.1396 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7bcd0797-cc83-390f-8858-e9f0e4c2b0b7 | -6.90695 | -59.15271 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 3072e84e-57d8-3620-b3bc-de8d2cc5a5e8 | -7.13237 | -59.64742 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23dcfe13-9583-3459-a3af-b9ea7ffa109f | -7.32114 | -60.6235 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfe0b01b-e966-3845-9e0d-dd7304667d6d | -6.89998 | -59.13388 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 20192117-2845-3b9a-926c-8e50d2931ac0 | -6.88706 | -59.14906 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 25cdb84e-3de0-3072-a5da-6c235f64dffa | -6.08519 | -59.94606 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| edffd5d7-53db-3002-9ebe-8d317ab6e3b3 | -6.09345 | -59.93036 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f42afde-1814-31b1-a0d2-6e35e6873661 | -5.7492 | -59.89779 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 323bc933-fff4-34c4-9726-96cef0fcd0b7 | -6.89302 | -59.14433 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4e5a7cd4-0b5e-300b-92cb-65365296bb67 | -6.09704 | -59.94111 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efa44de3-a51c-3bd0-80ea-cec20dc0da7b | -7.13912 | -60.12577 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9ba1017-4da6-3ff9-83c6-6d2ddd0b7794 | -6.92885 | -59.14472 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8873ea22-f69d-3b29-b8c8-4020bc2cd49a | -7.23609 | -60.00243 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04adce58-7af2-3a36-9f0f-a51f5321e688 | -5.75748 | -59.88209 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e82faa0c-86af-3b2a-a5fa-9b2249782ebe | -6.65636 | -58.8206 | 2025-08-14 04:49:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdd3c02f-3058-34a8-a71a-d41b47c5332e | -7.1254 | -59.62708 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f69c9ff-cfb8-3ea6-96d1-a0d8dc1670c6 | -9.31387 | -46.22399 | 2025-08-14 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d6969ed7-0f67-34a9-8205-961b373f2e05 | -7.11721 | -59.4195 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 987df93d-9ae8-3090-81c8-8f3cc682f569 | -6.08935 | -59.95362 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b91d588c-004e-3be3-88a3-6d5bdc741492 | -7.13382 | -60.12484 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff24002b-2c02-3252-a11e-ea390ae65f2c | -7.33268 | -60.62311 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28a8aba9-29f8-3226-9860-6217df326fce | -7.72531 | -55.20427 | 2025-08-14 04:49:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a23fe8d-db3a-3fec-8cb1-61af7fadd9e4 | -6.9274 | -59.15132 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0382522-2972-33cd-a457-813b3a44d174 | -6.09169 | -59.94034 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8d307bc-fb96-396e-86e1-2fe568529f83 | -7.31567 | -60.62371 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c3ca2ee-fd36-3496-a83d-af2bb2e12d68 | -7.42444 | -60.03595 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e726216-4bc0-3484-9859-0810ba57a46e | -5.74126 | -59.89688 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 490fdc0d-3b5b-3bec-a0ff-bf89be838164 | -8.09354 | -54.9852 | 2025-08-14 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68fd56da-c5a0-3308-b7c6-d1b8114265c6 | -6.91988 | -59.13731 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 57f879ba-b447-3abf-a0e8-9e49078987f1 | -6.91799 | -56.61767 | 2025-08-14 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa2c97ef-eb9f-372d-b9f7-0fc13af47d18 | -5.76047 | -59.89626 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71ee0b9b-18b9-3475-839f-706d0e2a0b63 | -7.12054 | -59.41897 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fad03ca-65ff-3ceb-b2c4-b5490cef4432 | -7.46083 | -59.89141 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3b14f7e-e7c1-381d-8b5b-474fad17f749 | -8.7444 | -44.02525 | 2025-08-14 04:49:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 84aa1b68-3f8d-35ee-a999-c99382835ddb | -6.94173 | -59.62903 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8560ac82-aa08-3d7f-ad44-91e5b5df450c | -7.33205 | -60.62552 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a54e939-3ce2-30c7-b213-c6f432e3e8e0 | -6.8811 | -59.15375 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 326a9c93-d562-395d-b9c0-2971a016cd9c | -6.10529 | -59.92535 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4681e8ed-5c3c-3bf9-93ef-6f30e41d16ee | -7.52554 | -61.38195 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 392b6b4a-b90d-33f4-abec-356404021392 | -6.87315 | -59.14061 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 611207ff-98f2-3dec-a97d-47d84748c5e9 | -6.09937 | -59.92788 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab322124-4f96-30b2-9859-f43ee4a8c040 | -6.65147 | -58.81977 | 2025-08-14 04:49:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3cf01cc8-d1ca-3392-ab13-5de17f30f83c | -6.89701 | -59.15084 | 2025-08-14 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 95825b09-99dd-32cd-b007-f14b1236b1fb | -6.11004 | -59.92952 | 2025-08-14 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abef56f1-eaa6-3ad5-8090-610092a9e5e0 | -12.34941 | -49.91931 | 2025-08-14 04:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b450dcc-aca0-3f60-ad53-e42e829acbec | -8.1092 | -61.19921 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2cc56742-d629-3636-90cf-aab5bd6e844b | -9.06114 | -60.64739 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0452815-355f-309b-88a1-488725bb6783 | -12.32148 | -46.05492 | 2025-08-14 04:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bcb0130-bb3b-3386-b0a8-e8e594216d30 | -11.68124 | -51.62156 | 2025-08-14 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f1f7f9a3-f2ef-3a17-b801-1e459adfe8d8 | -7.87213 | -61.80771 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 61c30a81-a7c2-3ad2-ac22-03b6bfb7662e | -13.07457 | -49.32627 | 2025-08-14 04:49:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc3fe2b9-ec41-33c2-96f8-cd9b7c0db7a1 | -9.49993 | -60.52095 | 2025-08-14 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b084a01-ffe1-38ca-97b7-33e8a0e1c2e3 | -7.87565 | -61.81533 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 06a4e9fa-404e-3218-adcd-d4d73b207bad | -11.56101 | -52.09045 | 2025-08-14 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b24345b-0923-3b54-bddc-40a8bc9c12ff | -8.10431 | -61.19442 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9653f105-edb7-35e6-9a41-9919fe383d99 | -8.10713 | -61.21041 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 42a9ac91-e68e-3e0d-9048-4ac3adf72896 | -9.20345 | -59.65487 | 2025-08-14 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a5c9bfe-0910-3fa0-856f-0fb2f897fcdd | -12.58128 | -46.95649 | 2025-08-14 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d729c589-c2ab-320a-9fb8-39a3fa8f7019 | -11.68457 | -51.6221 | 2025-08-14 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a6ee57a1-249b-3deb-af2b-31e94ecde2c2 | -7.87498 | -61.82535 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c15825c7-5ac9-35c0-925f-215933b6359b | -7.60609 | -63.52364 | 2025-08-14 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d74b3cd3-3db3-3605-b52c-26a5f398fd17 | -13.43969 | -44.50298 | 2025-08-14 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| da4edd97-d977-3ef6-ae85-804b2d400e44 | -8.1064 | -61.18317 | 2025-08-14 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f598eff-094c-3615-a370-7e79158d16ab | -12.30283 | -50.01574 | 2025-08-14 04:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7ea5c69-09b1-3493-bf5a-1d7e7ce1846e | -13.07818 | -49.32683 | 2025-08-14 04:49:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee567a40-2a5b-3da7-9a28-04c7f75912c0 | -12.3506 | -49.91146 | 2025-08-14 04:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README22.md)
