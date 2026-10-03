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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c27c4a57-217c-32b2-9f1c-05140dee71fa | -1.26585 | -54.56213 | 2026-10-03 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 42365aa7-eaaa-3d46-848d-b0ba78b3eb27 | -2.93041 | -54.15462 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b7f009a-6ced-3c89-968b-34b1a6ab6659 | -2.25383 | -51.93531 | 2026-10-03 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86c31252-3e3c-3e0d-a797-91d71e69abae | -2.24291 | -51.93369 | 2026-10-03 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c95b7fc5-ba8f-39b4-bb46-1cd661631d31 | -3.00084 | -54.23202 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7c85398-0f16-3278-9277-a3858543d651 | -0.37154 | -52.02436 | 2026-10-03 05:33:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ed0895b6-f328-3621-a570-d1c2c90e39e4 | 1.9043 | -55.81351 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63dd08be-4f12-3582-b97d-324825c0e37d | -2.24837 | -51.9345 | 2026-10-03 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcc9c961-5548-3d5a-82b4-f6c45bde87bc | 1.78607 | -55.60316 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 377c43b3-9faa-30fc-a5e2-200a0f645564 | -3.01374 | -53.89294 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17b36039-2c9f-35c2-9106-f741864745a8 | 1.80036 | -55.59032 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a99ac0f2-5d62-3c57-9abb-12cb39e9e357 | -1.21652 | -54.53858 | 2026-10-03 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3434569c-b299-33e2-b6f7-c1b5b192d998 | -3.18015 | -54.08688 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 845d1cb4-a57a-3442-8955-81a8e0d63be1 | -3.28676 | -53.84011 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 259f5984-6511-307a-b1d4-bad314d528a2 | -3.28108 | -53.84466 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0afd5dab-3de7-342d-ba26-9576ab6eccf8 | -1.60897 | -54.76175 | 2026-10-03 05:33:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9e32784-37ee-3b79-b4b7-a55a8b72238c | -3.28629 | -53.83123 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 101be984-04d0-3baf-b1d2-6ff56041fb69 | -3.13899 | -53.74443 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a764db84-ddeb-3034-b957-4bbcab08b3b0 | -3.1341 | -53.74371 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cbf01f2-778f-3a5d-99ac-e66b5a9e7c08 | 1.94331 | -55.73033 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa2d1824-0086-3d75-a17a-c2c8de85049a | 3.69998 | -51.59471 | 2026-10-03 05:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ccd07a88-bbca-34bb-878b-9041a11cecd6 | 1.92704 | -55.80481 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85e4aa03-c0b2-3b77-ac0b-d40c158a5eb8 | -3.13328 | -53.74913 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb12fcbe-4d63-37ae-b16c-c5c77d4bdd2c | -1.76493 | -55.03121 | 2026-10-03 05:33:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d25cb8a-f420-3871-a4e6-8a80b8074c45 | -3.17379 | -54.09674 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47e3d78b-c648-3cf1-bb66-69124815efb8 | -3.10668 | -50.29812 | 2026-10-03 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d97ff6b2-2727-3235-916d-fdc0d902d604 | 2.54724 | -60.61124 | 2026-10-03 05:33:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9738d45-21f8-3b34-aacd-93d8b0c7f7c5 | -3.88065 | -49.69009 | 2026-10-03 05:33:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c1e5fa8-c1f3-3dd4-a7fb-7d8c6ad93aa2 | -2.97443 | -53.27286 | 2026-10-03 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8d20f09-c3db-3a91-a316-910d7deb4982 | -1.27034 | -54.56277 | 2026-10-03 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0bab4e6e-a2cd-333f-85d8-203c0a93162a | -2.97277 | -54.0988 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6b9c8a2-c8f7-35c1-a542-bc5510c52698 | -3.17692 | -54.07579 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 499d04a2-770a-3c9d-b630-55a8d1b0ca1e | -0.35722 | -52.01236 | 2026-10-03 05:33:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 52bda9a8-70d3-3ece-92b5-21a5d8f924d4 | -2.25437 | -51.93179 | 2026-10-03 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec94f1f3-14ea-38f3-a5b4-28694f696185 | -3.22832 | -54.31101 | 2026-10-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86b9c196-824e-37e9-8a71-230fe71fe951 | -2.33684 | -51.94844 | 2026-10-03 05:33:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75df0885-f220-3b55-ad59-7c3bdfe10c72 | -3.69863 | -50.97631 | 2026-10-03 05:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c86a847-3002-3200-bacb-28343f1c3278 | -0.3525 | -52.01048 | 2026-10-03 05:33:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 46663b45-8fe6-321c-af7f-09e450b4027c | -1.05781 | -53.58927 | 2026-10-03 05:33:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec1a443a-c4e8-39f5-9a46-c91739dfc1c5 | 0.22907 | -60.50156 | 2026-10-03 05:33:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2a1fcab0-ac43-3ce5-9059-eb553245180e | 1.78209 | -55.60378 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08855c09-43e8-3757-8796-9906af30560f | -3.13084 | -53.73213 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 00e383da-128f-35a1-9a6e-d74f9563b90e | -3.71097 | -50.66175 | 2026-10-03 05:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed05dda3-618b-33b1-84a0-00323b49f0aa | -2.89152 | -54.11728 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 697892b8-5e0f-3ba5-8bca-84ae7b5f7531 | -3.28393 | -53.84734 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8875df1-71d9-392b-845d-afc2e61958aa | -2.88677 | -54.11657 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6c82627-4824-32ec-b00d-663505f15458 | -2.9698 | -53.26937 | 2026-10-03 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8bd9579-ccdd-3438-bf94-13c21d421a0e | 1.79981 | -55.58687 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8bc02c3e-9160-33c3-960b-c777f956cf1d | -1.26655 | -54.55762 | 2026-10-03 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4aae6510-82e4-30c5-b683-874994bd8ffb | -2.05215 | -56.8681 | 2026-10-03 05:33:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6c69079-a24c-3153-87cb-ec7cc673e510 | -3.00568 | -53.88087 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 568bd9ff-32da-37e9-b318-a972f52d4d10 | -1.73604 | -57.17538 | 2026-10-03 05:33:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f29964f3-04e1-38cb-bb0d-ead75efa09ef | -3.4097 | -52.83406 | 2026-10-03 05:33:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95179e3b-d0d7-3281-99c2-07aa88dc0a55 | -3.21575 | -53.94807 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5867bf25-9f62-31c8-9824-82107a41a614 | -3.11862 | -53.74694 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 19ce589a-8760-3fac-a7c5-059394ec879b | 1.21959 | -59.97543 | 2026-10-03 05:33:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae7bde94-fb5e-37fd-b6b5-14e2312782cb | 2.35969 | -50.7526 | 2026-10-03 05:33:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be408b1a-e258-34e1-b956-d79d2424aa2c | -3.8813 | -49.6855 | 2026-10-03 05:33:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67542f24-898e-38e8-bf3d-844ac557651f | 0.62739 | -54.40704 | 2026-10-03 05:33:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c4eaa0e-59e0-30c5-b894-4107b2ee046c | -2.90096 | -54.08746 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4cb03a9a-1745-303a-96b0-0b531fd5541c | -3.29726 | -50.32211 | 2026-10-03 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85d99d1c-e3c2-3405-b516-47084ca819de | -0.35194 | -52.01158 | 2026-10-03 05:33:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 15eeb6c1-4156-3db7-85d8-12fd9fac59fd | -3.05592 | -54.16583 | 2026-10-03 05:33:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9f3cd458-d2fb-37ab-badb-f6afafa18820 | 1.92522 | -55.74357 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99f9dd9c-0038-306c-8eae-f850588f5bbe | 0.90957 | -59.62799 | 2026-10-03 05:33:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0835a030-57b9-3242-ba84-14be2e99e651 | -3.13492 | -53.73827 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a5a1d104-40ec-35d6-bf5f-854f2b9f08f9 | 1.7895 | -55.59908 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0691ce00-cc07-3814-8517-92a178ae05b6 | -1.26067 | -54.56596 | 2026-10-03 05:33:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a3cd25d-44ad-36b8-90fe-8d6d9a9aa603 | 3.79353 | -60.97286 | 2026-10-03 05:33:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19620728-db37-3258-99dd-218675e11367 | -3.07453 | -51.27577 | 2026-10-03 05:33:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 08d1c0c2-3296-3737-bd04-fb017729f2f8 | -3.02688 | -51.27282 | 2026-10-03 05:33:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25af4711-5087-3d8d-9384-54f9e0408881 | 1.91133 | -55.80725 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0bf2974b-4542-3b4d-96be-eadbb524a38d | -3.10809 | -50.2886 | 2026-10-03 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a9e90a2-4eb8-3c2c-8cbd-94df24645cd6 | -2.33738 | -51.94494 | 2026-10-03 05:33:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fab078d-34f0-37bc-a803-9a01023f918b | -3.22515 | -54.31318 | 2026-10-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b862348-71dc-3243-8ee7-9f2ed3502d27 | 1.80103 | -55.56899 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad1eb17b-fc7b-3b22-a870-ebe8b6dc0d74 | 1.90741 | -55.8079 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb5fe7c3-1661-3460-be8f-ce6f51ba7348 | -3.13002 | -53.73756 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5e7541ce-86b1-313e-8838-1736f6415ff4 | 1.77866 | -55.60785 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcb9af65-b074-3118-9f78-9b16a9ed4410 | -1.73984 | -57.17599 | 2026-10-03 05:33:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca370365-77ef-3eb6-96ef-308af764d046 | -3.1618 | -54.0789 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7078c887-0c64-34f8-809e-8f1376c9db69 | -3.28997 | -53.85154 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 856b86a4-ce2a-375c-8fb6-dee8e5762582 | -3.7002 | -50.98167 | 2026-10-03 05:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff407376-795e-3d13-886b-a3842bcf100a | 1.78441 | -55.59283 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 767dd3a0-8f52-3da1-87ac-bf1152e32588 | -3.17857 | -54.09741 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 995fb6c8-1020-3b1c-98b7-b970955277d6 | -3.11494 | -50.28477 | 2026-10-03 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7f316cc-4010-3ff6-ab7b-1cbcc5f29473 | 1.91201 | -55.7867 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a2ed59a3-9a32-3051-90b4-b8d1601e87e1 | -1.60969 | -54.75716 | 2026-10-03 05:33:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea6aa39e-87d4-3658-84c0-93fdff7dcdc6 | -2.1699 | -49.7687 | 2026-10-03 05:33:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a174e2c-14b1-31be-b11e-afe210480797 | 2.35469 | -50.75566 | 2026-10-03 05:33:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7ee0054-a835-370d-9608-99d988c09671 | -3.2109 | -53.94748 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cc3fa527-4531-3037-9b10-1436efa4db05 | -3.29365 | -53.84888 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d28eb392-dfbd-31c4-95fd-4c0eeed1c700 | -3.16657 | -54.07968 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7838b75b-d0c0-3377-9726-85692a51abcf | -3.12839 | -53.7484 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2e490d13-32e1-335e-8300-8dd04e28f367 | -3.00648 | -53.87553 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 810f74ce-04a1-3bbc-b209-28e5973c224a | 1.93229 | -55.73729 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d0e9539-dbe8-32a4-84bb-1e9aee9b5be0 | 1.7883 | -55.61694 | 2026-10-03 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 78b8a572-5ec0-351d-ab9a-16d3a423cc19 | -3.28064 | -53.83582 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c4c41df-4bbf-39d7-b06a-b005817c1606 | -3.18337 | -54.09794 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1e68599f-eca4-35eb-b2d5-1faed189b425 | -3.01857 | -53.89365 | 2026-10-03 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README43.md)
