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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd643089-19ea-38dd-a019-4ba25827eb6b | -13.2755 | -50.8137 | 2025-08-19 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 184fefe9-fe7e-3c48-8dbf-5a360717b0b4 | -8.6129 | -62.6308 | 2025-08-19 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 322c0c34-32d8-3ea1-97b0-d6285c402aad | -3.982 | -42.516 | 2025-08-19 14:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 9f728ea7-1259-398f-b10d-e74c22690532 | -13.1746 | -54.9337 | 2025-08-19 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 206.3 |
| e5726f4a-f80a-3e83-abbc-2e3e984af4b3 | -12.9971 | -56.8395 | 2025-08-19 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 0760dde2-d1ce-3a75-ac65-d0d3c2d3ccac | -12.9778 | -56.8614 | 2025-08-19 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 7f4c9db1-afc7-3402-bd2a-250229d19af3 | -6.5203 | -45.4787 | 2025-08-19 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 5e231e49-c738-3132-9b70-caf753b390ff | -13.2567 | -50.7947 | 2025-08-19 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 3ecd835e-b411-3608-b61a-38bf69b7b08d | -7.0612 | -59.2358 | 2025-08-19 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 617469a3-1065-3d18-9b94-f66b3d4e4a0a | -12.9925 | -45.202 | 2025-08-19 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 5e52d89d-c4fd-38d4-896b-e04d67bf6773 | -13.3534 | -54.4419 | 2025-08-19 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 153.0 |
| 39a1872b-2a27-3f99-b4a9-056dd6826405 | -6.9527 | -43.585 | 2025-08-19 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 126.8 |
| d134f9c7-9c43-3cf5-8178-96358061f343 | -9.1709 | -59.6374 | 2025-08-19 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 24246d10-1993-327e-84a7-81673325a7d0 | -5.7887 | -43.6134 | 2025-08-19 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 51317761-f88d-3611-b7e8-fcb44245e499 | -6.9712 | -43.6066 | 2025-08-19 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| e6411a6f-0b88-3ed8-bbd3-f60604737b5f | -9.1711 | -59.618 | 2025-08-19 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 488ecb83-9b6c-3ed2-8715-4174a91a563a | -9.1895 | -59.6364 | 2025-08-19 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| c789df1a-57ad-361b-ba5c-6fc00fbd91bf | -13.354 | -54.4006 | 2025-08-19 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 136.9 |
| b018cf28-f91e-399b-ba4e-050128404ead | -13.2563 | -50.8162 | 2025-08-19 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 928ddad7-1380-3c4b-91c6-90149995fd82 | -12.9971 | -56.8395 | 2025-08-19 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 50ddfa5b-a1ad-3e1c-9f70-9aadbc4189e9 | -13.3729 | -54.4192 | 2025-08-19 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| c114593b-ad78-31e7-899c-d2b3cec969c5 | -11.0107 | -45.6333 | 2025-08-19 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| b5667c54-4f29-38b9-9418-48a5c41ef2f7 | -14.1707 | -45.3042 | 2025-08-19 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| a661b8c0-4a4e-3757-9e6b-f5b12e21832b | -12.5042 | -45.5788 | 2025-08-19 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 4b0f9791-52e5-308c-9dac-3555509f4c6d | -12.978 | -56.8413 | 2025-08-19 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 6b01f64a-c15d-3b0c-a1ad-31e134206b99 | -7.0427 | -59.2366 | 2025-08-19 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 093512da-a234-30e9-b605-728a0357efa7 | -13.2948 | -50.8113 | 2025-08-19 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 144f9ba1-a2a8-340b-a42c-857d6d9151c2 | -15.0196 | -54.8112 | 2025-08-19 14:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| bb697bd2-3fcc-3e02-8612-0c23052548a5 | -13.3537 | -54.4213 | 2025-08-19 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 330.9 |
| b07db9cb-62ce-34de-a4bd-61fb05cf3a3b | -9.3395 | -48.5234 | 2025-08-19 14:10:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| a33fa2c7-faaa-39e9-832c-d653b16a1357 | -6.5201 | -45.5013 | 2025-08-19 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 349.5 |
| 486e1a39-a22d-37c1-9c8e-8f987cf05564 | -9.1898 | -59.5977 | 2025-08-19 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 92f8a545-4315-3489-be02-cda7dc8f3b12 | -6.9715 | -43.5833 | 2025-08-19 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 177.4 |
| dbcc5aac-8a33-3184-9b64-1ed79e1187ac | -9.1708 | -59.6568 | 2025-08-19 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| c5897619-da93-3a34-9256-515cbed45524 | -10.9916 | -45.6359 | 2025-08-19 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 8dfaf255-3320-323b-abab-d30fb0715230 | -6.9339 | -43.5868 | 2025-08-19 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 41524836-8229-39e2-8758-e0319dc94033 | -3.982 | -42.516 | 2025-08-19 14:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 127.0 |
| 99e6b362-dc80-3c27-ae26-be2ab34e5ef5 | -13.2755 | -50.8137 | 2025-08-19 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 8d0abd8a-c78f-3455-9daa-7fcf4ccb4323 | -12.8984 | -46.0906 | 2025-08-19 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| ec40cb35-e8b6-3f88-b8c2-f61158b4aeb0 | -13.354 | -54.4006 | 2025-08-19 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 125.5 |
| b18421f8-a8bf-33e0-a15c-7c6944f2e942 | -9.1898 | -59.5977 | 2025-08-19 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| ebf5f421-cfc3-3644-8f1d-f2f266ef5f34 | -7.2602 | -50.1613 | 2025-08-19 14:20:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 9d372033-c642-3713-a2da-287a6bef3703 | -13.1555 | -54.9357 | 2025-08-19 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 503.1 |
| b68f206d-bf2a-314e-840d-6b82a30cf9b1 | -5.6406 | -43.4153 | 2025-08-19 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 151.2 |
| e3b85422-c6d3-3922-b0df-cfd1e3af7358 | -8.6546 | -54.5898 | 2025-08-19 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| e4b0c709-30f8-3c68-8160-f19625248edd | -7.9251 | -63.2796 | 2025-08-19 14:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| d5d4e531-cc6c-3841-80ea-cf28f0b15c98 | -13.2755 | -50.8137 | 2025-08-19 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 134.8 |
| fafc5efe-858e-3bd0-b0b2-fbbe94dc22bb | -13.1746 | -54.9337 | 2025-08-19 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 312.8 |
| 6a12fed3-c01b-3c3c-9582-b4faa86ed59a | -13.1552 | -54.9562 | 2025-08-19 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 4f29838e-cc82-33b6-a6bd-49e8df028040 | -12.9968 | -56.8597 | 2025-08-19 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 416b6072-be75-3c8e-9314-ae8164ad4b7b | -10.9916 | -45.6359 | 2025-08-19 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.0 |
| e06360a3-7044-3172-9623-4f66a23bac9a | -9.1895 | -59.6364 | 2025-08-19 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 235f3d7c-fc87-367b-88f6-2e21c395c2e2 | -9.1712 | -59.5987 | 2025-08-19 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 6cef1ac6-4b30-3e89-8e76-48f9c3ecedc7 | -12.978 | -56.8413 | 2025-08-19 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 57fea436-e66a-3202-b7c8-e349c02da91d | -9.1708 | -59.6568 | 2025-08-19 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| f93d6acb-1b96-3b88-afd8-6b5777669a28 | -13.3537 | -54.4213 | 2025-08-19 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 233.6 |
| ba5215ce-ffbf-38b7-8f2e-3ec6fd27e531 | -12.898 | -46.1135 | 2025-08-19 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 6ab8a53e-04a2-30bb-b262-418f5bdc1743 | -12.9971 | -56.8395 | 2025-08-19 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| aac71975-d46b-3d7f-ab1f-767e84285e7e | -13.1743 | -54.9542 | 2025-08-19 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 5680a5d5-b25a-3575-8114-90ec6ef815b6 | -6.5203 | -45.4787 | 2025-08-19 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 64d81cba-b063-3a36-a50d-31f8afd94319 | -12.8984 | -46.0906 | 2025-08-19 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 173.1 |
| e9c636d2-ab04-3b44-a1c3-fdda2d7b8d78 | -15.0386 | -54.8297 | 2025-08-19 14:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 151.3 |
| ea608d49-68e2-342a-9de1-80d5e6da308b | -15.0196 | -54.8112 | 2025-08-19 14:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 4b0984fa-92ab-3396-8917-2cd23b78c42f | -12.9778 | -56.8614 | 2025-08-19 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 69dac2c5-b2a8-3f48-a532-013c6cf5dd59 | -13.3534 | -54.4419 | 2025-08-19 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 1fd570f4-2122-301d-872f-d5893e4b796b | -3.982 | -42.516 | 2025-08-19 14:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 133.4 |
| 794ab4a1-d9af-329c-b927-0d34aa89d51d | -7.5899 | -45.4315 | 2025-08-19 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 881443df-f3a8-3497-b900-4c380856bb32 | -14.1707 | -45.3042 | 2025-08-19 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| c44ff7b4-0da1-3fe3-97de-ee7a8e25795f | -11.0107 | -45.6333 | 2025-08-19 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.8 |
| ebdf309b-a426-37a5-a624-0844e9b99b5f | -5.6408 | -43.392 | 2025-08-19 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 149.0 |
| a2877e3e-1318-3172-8e68-7eda6c262adf | -5.7887 | -43.6134 | 2025-08-19 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 22555f2a-dad4-3d4b-950a-963972089eba | -13.2563 | -50.8162 | 2025-08-19 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| f70c7c41-a4f8-3567-a4cf-b268b6ef9bd4 | -9.1709 | -59.6374 | 2025-08-19 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 6929ca7c-986e-3386-8607-ec30c469e263 | -13.2567 | -50.7947 | 2025-08-19 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 2c4b43db-bbce-39e2-9a94-c63c00ea43fc | -6.9527 | -43.585 | 2025-08-19 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 781bc3c0-b981-3950-a4d5-f90b3c479720 | -7.0427 | -59.2366 | 2025-08-19 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 2eca6671-cc86-3245-8f14-5e43992784d6 | -12.5042 | -45.5788 | 2025-08-19 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 2e0e482e-9220-3335-a578-5238cbea11bc | -9.1711 | -59.618 | 2025-08-19 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 87ad5e8d-30f9-3d03-82c2-827a0c983eb1 | -13.2948 | -50.8113 | 2025-08-19 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| b6f773d3-f8e6-394f-b5ed-35bd1994d1a0 | -15.0389 | -54.8089 | 2025-08-19 14:20:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 19ad4899-30aa-3b97-9515-a71eb66ebff7 | -6.9712 | -43.6066 | 2025-08-19 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.5 |
| b8f60e1c-a91f-3f18-98ac-fe18c1ba998d | -6.9339 | -43.5868 | 2025-08-19 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 677ba851-df2f-3a11-88a1-aa9f0b90455e | -13.1558 | -54.9151 | 2025-08-19 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 161.9 |
| d5c91e7d-ca7b-3528-8881-62f2eefaa748 | -6.9715 | -43.5833 | 2025-08-19 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 1c33840c-b383-347d-815f-802a23e640d1 | -7.5711 | -45.4333 | 2025-08-19 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 54e0141e-b94f-36c7-93e2-45bccb126786 | -3.982 | -42.516 | 2025-08-19 14:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 120.3 |
| f7d90896-84f8-395f-a354-95368ff9492a | -11.0107 | -45.6333 | 2025-08-19 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| e32c0472-2bb3-36c4-83dd-d79f8850e69e | -5.7887 | -43.6134 | 2025-08-19 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 163.4 |
| de1762b8-4422-318a-9a76-f029a20dbb0c | -12.8984 | -46.0906 | 2025-08-19 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 7980c042-7e88-32a9-951e-ac3af5639b5d | -6.9339 | -43.5868 | 2025-08-19 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 141.0 |
| d7559687-735b-3b0d-9b28-67a14319889f | -12.978 | -56.8413 | 2025-08-19 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| e4c93f34-5287-3a19-af7f-02f6c8a64f87 | -13.2567 | -50.7947 | 2025-08-19 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 168.1 |
| edd97613-b617-38cd-b283-fe5852fba682 | -7.0427 | -59.2366 | 2025-08-19 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.8 |
| be9bb87f-fee4-39ca-865b-7696b1d2db0c | -13.1746 | -54.9337 | 2025-08-19 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 184.9 |
| 6db394ef-0fbe-3787-8a84-d26ee5681f4c | -9.1708 | -59.6568 | 2025-08-19 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 16f8555d-3d4d-3b4e-8c2a-75d0a0d3dacc | -13.2563 | -50.8162 | 2025-08-19 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 117.2 |
| b38a911b-9b82-38bb-9cd0-52609f619e51 | -13.1552 | -54.9562 | 2025-08-19 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 203.1 |
| eb85b959-0be2-3ab8-8908-78277ab14dab | -6.5203 | -45.4787 | 2025-08-19 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| a9750117-6f7b-38af-8569-a7023447ec43 | -9.1711 | -59.618 | 2025-08-19 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| dc895435-ca38-3528-a77f-0f558f9e0282 | -13.1558 | -54.9151 | 2025-08-19 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 181.7 |


[Clique aqui para ver as próximas entradas](README61.md)
