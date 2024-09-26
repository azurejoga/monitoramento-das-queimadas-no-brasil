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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a58c3149-8764-31cc-98c0-eb287e65e9bd | -6.7668 | -59.69572 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a60ee0b7-f00d-3bb8-b7d3-c8520f4f7a92 | -6.7633 | -59.69128 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7bc47a1b-78f2-39e7-bb4d-5c36ad33e6ca | -6.75628 | -59.68243 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8e7fbb0-95b7-39c8-b448-4aebe0a5cbe6 | -6.74089 | -60.08755 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4c2b6c4-7017-38b7-892e-dd5d62c66cc8 | -6.73733 | -60.08287 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1bea156d-9a45-3684-9251-5331dc802c98 | -6.73665 | -60.08683 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95fe6413-8b86-343f-b8e2-624d7968456a | -6.73242 | -60.08608 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b02dfdf-1105-3ace-a148-31762682c660 | -6.72728 | -59.85686 | 2024-09-26 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f206f7c-b30a-3a7b-9e8c-5cae649bdeee | -6.72375 | -59.85232 | 2024-09-26 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d5f97a46-d05a-3025-bc29-10c3a42edf01 | -6.69101 | -59.84288 | 2024-09-26 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc0922b0-2578-31ce-b2a8-8e1c767ffcac | -6.682 | -59.84543 | 2024-09-26 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a43ba86-d57f-3781-aeec-a9b58bf820d6 | -6.63856 | -59.97366 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f10d58a-bfce-3ca7-ba97-ec3bc9bc26de | -6.63435 | -59.97297 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fbc9d75-147a-3ad0-b8a3-ba488b640d0f | -6.63368 | -59.97688 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3dbad999-b638-361e-83a5-6f13f3db39fd | -6.63096 | -59.99268 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 527ca1eb-caaf-3cad-8fc7-95ba4ef33308 | -6.6168 | -59.99898 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40bcb90a-70a2-392f-9a51-e8f5de1b72b5 | -6.61625 | -60.00245 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 578aa0c7-e5ca-3b45-ad17-cb36c947911e | -6.61613 | -60.003 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 419f3cea-e166-38ba-9c27-dfd556728da0 | -6.61273 | -59.99771 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f770698b-ba3b-32e6-aaa7-7ccfff00af91 | -6.61258 | -59.99827 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd77642b-fc93-3b2e-8e8e-8a6be5e52cb5 | -6.61203 | -60.00174 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 89f8334c-d4d3-3326-9b1e-dca57f0ace61 | -6.61191 | -60.00229 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e0a8559-a613-32a8-83c2-8481fc1d8fd5 | -6.60901 | -59.99358 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 273c0f39-53d2-3790-8855-532a1c53001b | -6.60835 | -59.99756 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0e58091-bf6e-359c-946c-010e84e1005d | -6.58355 | -60.0422 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0baca613-f849-3232-9628-80fa4805192a | -6.58288 | -60.0462 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e732b76-72f1-3733-ab9d-cd58c28279c8 | -6.57997 | -60.03757 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e388e609-36f7-3c3b-bb23-e350cd9812c2 | -6.5793 | -60.04153 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5af2601f-edbd-3892-8b2a-0148002089de | -6.57864 | -60.0455 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0874f35b-0c81-3d36-8124-60499a6d0f8f | -6.57797 | -60.04951 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4a4d612f-a9f3-36be-b0c8-6ea1d76c96f7 | -6.57572 | -60.0369 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f4064e8-5c8a-33d1-b1fd-d3432a9a50ea | -6.57506 | -60.04087 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b90ef373-7cc1-3353-92fd-b4556e3e651a | -6.5744 | -60.04483 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aae6dc05-c4ad-3cb6-9c9d-ee41d038505d | -6.57373 | -60.04882 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 67c50861-94c1-31b4-9179-d5e3989bddbd | -6.57306 | -60.05281 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 711864db-943a-3ea5-b487-13a4d9eca202 | -6.57174 | -60.0607 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a19ef063-d197-3096-a291-398df3dd6b61 | -6.57148 | -60.03624 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68f77ba6-78d9-33a6-ae31-793844ddf83e | -6.57106 | -60.0647 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a31e284-b374-3e34-a7da-727774bb37ac | -6.57082 | -60.0402 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 890dba68-104e-3e04-9190-e0f564f723a5 | -6.56948 | -60.04815 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ebea02a0-1f94-3146-8550-843951a542f5 | -6.56882 | -60.05211 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0de730e3-af9c-3686-8691-1956e904812b | -6.55326 | -59.96404 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e26bf31-f9df-33cb-9859-dfc85a337e70 | -6.55258 | -59.96805 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b9b6f21-a47b-31c9-aa2b-158530ecfeac | -7.50878 | -59.88484 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d582b7ea-980f-33ed-871e-e529646d1e50 | -7.50761 | -59.88153 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ee57055-f8ce-3f3a-ac3a-e805747bbb59 | -7.50696 | -59.88525 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97bcf69a-d079-3da6-ad54-f0a99c0472eb | -7.44447 | -60.01429 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4887208-f015-3e1e-acc2-218e7ddb95d8 | -7.40291 | -59.79079 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8de70d65-f07f-390e-86d7-ffed2c59906e | -7.40229 | -59.79448 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| adbacbf7-e0b4-38c8-81ae-e2004f54b527 | -7.40167 | -59.79821 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8b9e6169-19a6-3a31-81a8-f156f31c80c7 | -7.39881 | -59.78997 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b95bd250-2421-314e-8994-b9dd3f89be5d | -7.3982 | -59.79366 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c992b042-ccf1-3537-8de0-fc7b77abc983 | -7.31185 | -59.90252 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1df57fb-61fa-3866-9d96-da76cc97b82f | -7.3112 | -59.90635 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b35891a-6ec8-3050-a77b-671134a127cd | -7.3077 | -59.90187 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98dae8a7-c3ca-306f-9a2b-63471fb2ed60 | -7.30704 | -59.9057 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58021b99-c35a-3c44-b8e6-3dd3ec2315a5 | -7.27737 | -59.49257 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91d37b6b-38de-36fe-9890-886621d29a0e | -7.27396 | -59.48819 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e020ff84-c996-39d0-a8da-a5a7612069e5 | -7.27335 | -59.4918 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 05f35ed0-98f4-316c-8e86-002b6fe43bd6 | -7.27273 | -59.49543 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 552afae7-63cf-340c-8200-1457713e9192 | -7.27186 | -59.59871 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d90855c6-8310-30cf-95af-5b54b8b4cc0c | -7.26994 | -59.48744 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 580357eb-91e0-3f5b-9735-420957847f30 | -7.26931 | -59.49109 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72e24e4a-f4db-301d-825e-4fe6adc7c630 | -7.26869 | -59.49474 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d2bb8a8-b79f-35e2-8305-dd2880c4ce01 | -7.26588 | -59.48685 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42fe3ad3-7b33-32c0-9c5f-22def7161d57 | -7.26526 | -59.49047 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9f75efd-a4f9-39c8-8a03-f1267b5a1845 | -7.2043 | -59.42816 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57773d94-dbae-37ee-91ab-2f747027d8d0 | -7.20394 | -59.7498 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82a8dd09-d5fe-3fc2-953f-4926ec590995 | -7.15433 | -59.47816 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c4e8710-da0e-3aac-8a5a-43ce52bc0005 | -7.14968 | -59.48102 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43999051-49e7-33cd-85f3-50621a1cc11f | -7.14907 | -59.4846 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd3e8e36-5224-33b2-a776-10b633f5e28e | -7.12525 | -59.2271 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 856f0ba4-8d29-3703-898b-3b81de96d21f | -7.12498 | -59.45104 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96316bf1-6fc1-3ad8-98d8-8f289320f050 | -7.12409 | -59.23404 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e0e5676-224b-3ee3-b2a9-da15667d29fa | -7.12153 | -59.44678 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f86f8be-a988-3bbf-bc35-90df2c41cdb9 | -7.12094 | -59.45038 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d985eb7e-7fa6-37a5-9404-77fefea6d740 | -7.12034 | -59.45398 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4001700e-1b87-39a4-8d61-88864c219634 | -7.1169 | -59.44971 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0d3dce98-4243-36cd-81a9-c71783437fcc | -7.1163 | -59.45331 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6e706129-23eb-33ca-8f5e-80c9b045e0c9 | -7.09502 | -59.23639 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2c3c462-779a-3858-9eaf-682f96540229 | -7.09444 | -59.23986 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3751530b-4020-39ab-83cd-3e3a90bfbe7c | -7.09384 | -59.24335 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf4b4724-badd-3cdf-9006-474bd8cd2de3 | -7.09325 | -59.24684 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d115a99d-9f6e-341b-b82d-1dad6ef54e86 | -7.09221 | -59.22882 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c689b8a2-3523-37ff-8f19-842cf5705a20 | -7.09163 | -59.23227 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8149e2b1-83ed-3d1c-8541-deb361f5acb5 | -7.09104 | -59.23572 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70751795-b12f-39e1-b1c8-ee2cbefa8d6d | -7.09045 | -59.23919 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5b400b2-8e91-362b-8f51-df2e635d6586 | -7.08985 | -59.2427 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7818cb2-e449-3c3c-80bd-73c67777111c | -7.08926 | -59.2462 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0e08952-dff2-3d6e-8a86-c002a5173e7c | -7.08823 | -59.22815 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92be94a9-5f48-3ed4-98e8-e47ee1fa92f5 | -7.08765 | -59.23159 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd3ff643-9737-396d-ae98-2808d70429ee | -7.08706 | -59.23506 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 140d9732-c5ce-328b-b516-c4acbf0eb138 | -7.08646 | -59.23854 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f49f974-751a-399a-9333-95c5d65c59e5 | -7.08457 | -59.8224 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22c8bc91-c7e0-31c9-8364-f84d6f44baa6 | -7.08263 | -59.82171 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5bfd8640-48a5-31d9-a05e-c4fdcf776e44 | -7.08043 | -59.82169 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80201250-ae18-39b8-a2dd-b1682684682b | -7.58581 | -60.59353 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2461760-1b35-3646-b461-9c0156926f4f | -7.5851 | -60.59771 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2e3dd854-d6c0-34a8-bd31-9067ecf36ddc | -7.58148 | -60.59281 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a05791b-32b8-395c-9305-357926965f47 | -7.57786 | -60.58789 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README110.md)
