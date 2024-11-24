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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0dd97cb-58b6-34ed-be7e-4ee2061400fb | -3.12386 | -53.10722 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 258618c6-34ef-30b1-a2af-6aaf5aa86b98 | -3.57874 | -54.52249 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2d19013-e525-38c7-bbd1-809d10148e42 | -1.43046 | -53.38346 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17ea718e-b48f-3e77-b454-fa7adf075d8f | -1.31156 | -51.75115 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fbd8fe04-f1da-3446-8de8-e7af1798d0e6 | -3.31715 | -53.2846 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37b47bda-3266-3bb8-bee8-c2d6a65bae14 | -0.87741 | -52.76795 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9571eb5-c76f-339e-ab73-a32485beb0df | -2.54047 | -46.39709 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6fca14b1-7efc-367b-b4ed-11ad1f2dbe41 | -4.95213 | -47.80265 | 2024-11-24 04:53:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bc841599-021b-3517-87bb-a574c2390772 | -5.9506 | -48.047 | 2024-11-24 04:53:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5a0cb8f7-63df-370b-8180-dc2cc34737c0 | -3.29594 | -45.72448 | 2024-11-24 04:53:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 926de7de-de21-3a9e-85e0-4a5ec05d39cc | -2.70683 | -51.99068 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eef53e8e-cd4c-3bc4-810d-8322cd2fd7e4 | -1.38356 | -52.42459 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc60fa2d-be39-3d7b-8d83-a108ad5f0549 | -3.23995 | -54.24206 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17d57c9a-1742-316e-8f5f-0d094b3f99a4 | -4.63671 | -48.84165 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| e455eead-d9ec-3589-b764-464852662ab2 | -0.95082 | -51.64555 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66537ac0-be16-3d8e-8ad8-897c89905668 | -4.40511 | -45.62337 | 2024-11-24 04:53:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2de83e15-049f-3398-a84d-065aac15f4c1 | -1.94246 | -49.53275 | 2024-11-24 04:53:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a0cb23f-2002-366a-8c71-9022018df8f6 | -3.50373 | -53.79974 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e409f7d6-9020-3369-9d3b-66d7613b9fa2 | -2.21794 | -50.54068 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67a2aa42-9a89-33ba-88d3-f79e7ebde8cb | -4.58868 | -45.4936 | 2024-11-24 04:53:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00846262-3591-372a-9cc4-afacb4668401 | -2.7011 | -46.28138 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6fae2b16-affc-3f3f-bd06-c5008e512eec | -3.49737 | -49.93335 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 84b2fde2-2350-378a-b7a0-951fe3e52759 | -2.71186 | -46.26702 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d4b0023-21aa-342f-89a3-221c24421ff5 | -2.22787 | -50.7635 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60982eb2-3f41-31dc-99ef-9a3918159dcc | -1.19953 | -51.77179 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c20f9ff-6f61-3c7e-8bc8-82782a07c0b6 | -2.27983 | -53.62993 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44655e1e-dcf7-3aa6-82a4-3daccfb20b88 | -3.77275 | -52.17871 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47e93aa2-6ba0-3e08-94d6-3706e9293c7d | -2.73577 | -54.39397 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5613122e-57d3-378f-8094-1cd9ca494bf8 | -2.13843 | -50.67747 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae1db1ef-ad75-3e59-bc5c-8311700e25f3 | -3.53852 | -50.44221 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccf9936f-e0a3-36df-b2a9-3196a3c60917 | -2.17002 | -53.79259 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7800667c-b842-3db8-9dff-53c052f6eb47 | -4.26728 | -46.48543 | 2024-11-24 04:53:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9eb0a2c9-0a0b-3bcc-9f17-4085382652f7 | -3.52111 | -53.82119 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0a9fcaad-cb12-307c-90ce-5a89e556f43f | -3.25563 | -54.20991 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 742a3aa0-d24c-3fa6-bd2a-14603102119d | -2.11776 | -50.26101 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4fb7517e-522f-3e93-893c-f8c11dbc1470 | 0.05993 | -51.14644 | 2024-11-24 04:53:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c0c905f-7afe-3672-a394-f68dc616e62a | -2.379 | -50.38171 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0db17539-8281-329c-9ebf-87dde19510ae | -2.01403 | -51.17404 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 256b861f-5576-39cd-a938-a862754e4041 | -4.06547 | -50.00479 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a24384a-84a7-3e36-9bda-c47a98e3331e | -1.19973 | -51.96926 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8017a47-0554-3c8a-aed0-b11f5e4cc918 | 0.87368 | -54.63562 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c90e4cec-9070-31d1-82c5-6edddb69b10a | -3.22633 | -53.92854 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4925995f-f377-3715-9d66-882e331796b4 | -2.11905 | -50.65306 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc159b34-219c-3251-ad87-a5f7be45e563 | -0.85047 | -48.6258 | 2024-11-24 04:53:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ceaf7973-b2ac-3c58-84c7-38a36cbb66af | -1.97494 | -53.10464 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0577c64-c9b0-332c-87d0-de2ce2d26431 | -3.24459 | -54.23506 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48ae34e8-3e72-357b-a68b-ccad7c25f02c | -0.88846 | -51.72019 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| afcd0adb-1122-3ea4-9672-8e13bd0fb219 | -1.53238 | -52.45176 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 123ed388-bea5-34c5-ad25-401e190048f1 | -2.2915 | -50.67911 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4b84e0e-970e-3d2e-a381-fcc6ce227015 | -3.25384 | -54.22116 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b90cc351-8559-3f2a-8474-0947a14e5d78 | -2.23291 | -53.61889 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13ee42cc-8403-30c8-8836-a32f162de393 | -2.3151 | -51.31651 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b00a19da-cd83-3945-b9d6-0442f8d752ce | -2.97729 | -51.36632 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bc0395a-bf1b-32c0-8129-0573e4115c07 | -2.82092 | -54.02889 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 774f9296-f82f-3558-bd41-a0bab9813908 | -1.97439 | -53.10818 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e404e6dc-280e-3b15-839a-7df4880650a5 | -2.73596 | -47.53904 | 2024-11-24 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 351ebb36-08f5-3fa6-b1f8-ff9ae542b636 | -3.74917 | -50.00916 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c1fcfd6-6805-34b1-8363-0e2ed5c9144f | -3.23427 | -54.23349 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 66b6f939-d8c4-32d1-96a2-2d0f5fa9b9b5 | -3.50258 | -53.80699 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1903446d-ed70-39e5-8b6a-6a450ac051e7 | -2.43805 | -50.41308 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c789123-a6ad-3e0f-a633-199c7257c665 | -1.19569 | -51.7747 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b3a4f38-4e1e-3a62-af23-5f2ee52de70b | -2.40809 | -49.14554 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc9d0962-4446-30bf-aa92-8bc2e744df4f | -3.49665 | -50.46568 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe67a747-da84-351f-808d-d31d73f1f739 | -1.39972 | -54.50017 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6322ef71-5972-3505-be2d-c7133c75426b | 0.40996 | -50.85961 | 2024-11-24 04:53:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca38b2cf-b73d-313e-9df2-3b17fca979da | -2.29095 | -50.68266 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3bb22483-0fd8-3f3c-94a3-516bebc00988 | -2.04131 | -48.67724 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79827d82-60f8-3a2d-8e0c-50ecf5167866 | -4.53968 | -42.91007 | 2024-11-24 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4c2692d-c878-3476-bcb7-543dbe178671 | -3.67595 | -50.25537 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8689047-2e0e-3b25-a82b-533f9fd811f4 | -3.87747 | -52.35735 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4be1f778-6056-30f7-8b73-5672168024c2 | -1.23232 | -51.73897 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 111ac4bc-1846-3a3f-9059-c536dd38cdd7 | -0.09134 | -51.50738 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b73ffd38-58bc-3663-ae6f-71c721681625 | -1.27645 | -52.97806 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d9dfbd7-2a3e-304f-9b42-fbc2036a7770 | -3.22679 | -54.23618 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02300b8e-c6ad-3995-8156-7375360136ab | -2.55132 | -53.97994 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ce2ce89-1123-3bdd-b0a0-ea65e54514fb | -1.22849 | -53.68571 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ff331839-5f83-3d11-bb81-038653cfdfea | -2.69643 | -48.82453 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62340768-1d46-36cf-8bcb-8fc9d51bc0b2 | -1.73161 | -52.7217 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0915a74-3477-3b97-aaa5-8fb288718062 | -2.69734 | -46.27726 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a083033d-394a-3d25-a5ff-84cae13a2043 | -3.92651 | -50.08567 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56e6c40e-09b8-352b-b607-4e1b54f19a83 | -2.84499 | -54.00983 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8daf369-d8c9-36fd-80b3-6af2ab6a6fe8 | -2.62123 | -54.38482 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae268b38-5f1e-360a-b2af-139280c6064b | -3.50716 | -49.93879 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86dcecfc-cfc2-3311-895c-0317c0edc82a | -1.14034 | -48.76658 | 2024-11-24 04:53:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afacd10b-3fc9-3358-9a23-ce846b48e821 | -2.84382 | -54.01725 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d724093-6515-3a27-9ef7-4b9f6ff1397b | -3.80797 | -51.33797 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2d26efd5-ac61-3d84-9f88-9e67dc84b811 | -2.26567 | -50.80166 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59ad3962-a35a-3ae0-a962-017ad92e959d | -2.21698 | -46.38855 | 2024-11-24 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| dd4095a7-2d10-385f-82d1-2eb6177e76e4 | -1.95202 | -50.78568 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 253bad4b-58d5-33a6-b9a5-c3e52c1a6cd7 | -3.11086 | -53.70573 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e36ba1d0-c8bb-34e9-ba15-e3dfd5344da7 | -1.57603 | -53.8195 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d44da785-95a6-32fd-8586-bbab84f8a89d | -2.21997 | -52.27681 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c26a029f-7cf2-38c6-91bb-d01d0daa1599 | -1.24222 | -51.74049 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 863334ce-3960-30eb-87b2-0a9d2c718879 | -3.7006 | -47.12535 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 618421d4-c6f2-36d7-bce9-7b1b096866f2 | -3.95093 | -51.2269 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcbd62ab-ce6a-3849-abc1-1e7c68380982 | -3.11239 | -54.00515 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 54781c16-8fed-3d50-a010-e1845ec51b88 | -3.12775 | -53.10422 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4b31214-338a-3b9a-83c2-1205af5c27ba | -3.30156 | -50.365 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bbe6e0d9-d1c6-3add-8269-8911bb3708de | -3.03857 | -49.45134 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 87c2a89f-b608-33ff-a1cf-a0044b08bec7 | -2.62253 | -48.32389 | 2024-11-24 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README65.md)
