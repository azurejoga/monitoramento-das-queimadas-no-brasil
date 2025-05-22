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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b174d7c-85c7-3545-86f8-48b1a94b3d68 | -13.61519 | -55.45382 | 2025-05-22 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9cb66b6-f0a4-3bd3-89c0-7447898eadcc | -14.0485 | -56.06363 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12934b22-2bd2-3950-9b0c-1e4e37dcbbee | -12.65062 | -54.11613 | 2025-05-22 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba2eaf38-59fc-393c-b4fa-9202aad5fe9f | -13.69674 | -45.2733 | 2025-05-22 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f360e0f6-0dda-37d1-99b8-abc8aedc88d0 | -10.67643 | -57.60553 | 2025-05-22 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aedad827-1951-369e-b87a-c388241963f8 | -14.02919 | -55.14381 | 2025-05-22 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a658abd-6f67-312b-bb13-6cf08e680864 | -11.86242 | -54.78863 | 2025-05-22 04:46:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9387dffc-67bb-3169-9dc0-37f458680ed0 | -19.50937 | -48.66357 | 2025-05-22 04:46:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d90c45d3-59e1-3cdf-a8b3-0b4946627f7b | -17.71082 | -47.4958 | 2025-05-22 04:46:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e9b44d0-be2c-3e8b-a976-f4b43fa22426 | -11.2947 | -53.97667 | 2025-05-22 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0305dcb0-c76a-3071-b7ec-b2ed58e86b0d | -10.98395 | -59.16209 | 2025-05-22 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45c63420-e06d-38a6-ac91-8eea176635c2 | -12.28513 | -52.49923 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea032db8-2c27-3f9d-b959-ead512e4d23f | -12.35329 | -49.98364 | 2025-05-22 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fa210ae4-235f-337b-aa23-bfce4b19d0c9 | -14.85102 | -56.46132 | 2025-05-22 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02a2ff46-73a1-3b88-8ae9-d097a28b94b0 | -16.38229 | -54.576 | 2025-05-22 04:46:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63a2f6eb-74d6-3e22-ade2-b0245e6ddb6b | -19.156 | -47.81794 | 2025-05-22 04:46:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b391697-8ae1-35c3-ad44-e47db46cb1fe | -11.29812 | -53.97723 | 2025-05-22 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2ea981be-5d75-3b34-82a3-8990ba7624ee | -14.05661 | -45.51741 | 2025-05-22 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87d15e63-eafc-327e-9dcb-e4c26af7f05c | -15.69471 | -43.42281 | 2025-05-22 04:46:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19b51f7f-0648-3192-a5e2-6172ecbde3e5 | -12.0195 | -63.79479 | 2025-05-22 04:46:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e5d41c2-ea6a-3650-92a0-feb82f498cd2 | -12.49773 | -55.74016 | 2025-05-22 04:46:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad7c1128-84f5-358f-b963-f8049ee44d59 | -12.3498 | -49.9831 | 2025-05-22 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a26ee534-9fb3-3b76-acb5-fcde94d12c86 | -10.31358 | -59.56836 | 2025-05-22 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca3c9214-0df4-3b03-81d5-f5b6ec747299 | -12.34632 | -49.98256 | 2025-05-22 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 99c46594-95ec-39ac-bb8a-551f926f7be0 | -12.48971 | -57.18251 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87b807c9-bbbe-3e2b-a9be-15dcb4abc365 | -12.35386 | -49.97973 | 2025-05-22 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b16ecfe-9cc5-3eb1-90d6-a467e46e4387 | -11.29408 | -53.98043 | 2025-05-22 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c1a155d8-772a-386b-b4dc-3dae76c8c28f | -11.56996 | -54.56352 | 2025-05-22 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 264baadc-4214-35bc-afcf-f775020ff342 | -11.11527 | -54.65962 | 2025-05-22 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b358b9f5-d3a0-3d74-9f4c-7d1ea44e7888 | -17.6158 | -54.17498 | 2025-05-22 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a9a8b7c8-2461-38c8-8fe0-dd7ebeac7eb7 | -10.31297 | -59.56977 | 2025-05-22 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82d4b561-ccc7-3c67-b5bf-6f63aafe3994 | -14.01788 | -55.12569 | 2025-05-22 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 447e78d0-051c-31d5-97df-ede95eccd31d | -12.84147 | -47.39408 | 2025-05-22 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d678c489-ee80-3ba1-9fed-1c83094c0f5a | -13.77803 | -54.30418 | 2025-05-22 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9d14657d-9199-3d1f-bf27-22554ce30798 | -17.27709 | -42.65391 | 2025-05-22 04:46:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1161310a-10cb-32d0-86e3-d5e813619bef | -17.61639 | -54.17135 | 2025-05-22 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 411d3888-8745-3010-aa53-1970ea0f7a0b | -12.29116 | -52.50407 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ecc7360b-364d-3231-8d23-1d670c8633a1 | -11.57215 | -54.57192 | 2025-05-22 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec26af79-5131-393f-b5a9-25b46d243757 | -13.19572 | -56.82164 | 2025-05-22 04:46:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4748ca1d-4035-3c38-adad-cef55fb1e019 | -11.8942 | -49.20293 | 2025-05-22 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73dd730a-0fbe-30fb-97c4-d4281a8320bb | -11.57975 | -54.56922 | 2025-05-22 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4285652-542f-34f1-9e15-524b62e0d587 | -19.50889 | -48.66731 | 2025-05-22 04:46:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b024f89-79af-32e6-81c2-42437bc64f96 | -12.30002 | -52.49106 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 617008b9-461f-36be-acdf-e094d86acba8 | -14.05072 | -45.52677 | 2025-05-22 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9420ed33-2a2b-3281-bd12-6322f7c02504 | -10.68127 | -57.60251 | 2025-05-22 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28bac2fc-96ee-3c43-8cd7-f7abecb12158 | -12.35038 | -49.97919 | 2025-05-22 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c9b9765d-0aee-3c04-b7e3-0cfddeb0a816 | -12.68332 | -58.1269 | 2025-05-22 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54cd90c7-8aee-34eb-bd02-52f7aa14e0ea | -13.53681 | -43.68189 | 2025-05-22 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6230c4a-fb9e-37c0-afc6-b74577b2ce9e | -12.4846 | -57.18246 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 884bb0f4-cb03-3cb2-b33b-1e3ddf90b4a1 | -12.35792 | -49.97634 | 2025-05-22 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b815824a-47cd-3e86-bf4c-0761d19d7d5c | -15.56751 | -47.8541 | 2025-05-22 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 079934af-591f-3ce7-af14-163bce7b6785 | -12.10792 | -49.29662 | 2025-05-22 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 567ad390-5dad-3df2-a21a-1b2735097afd | -11.86199 | -52.27541 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03781d2f-b656-3bc7-aa26-f6a63865fa91 | -13.7848 | -54.30534 | 2025-05-22 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fccafafb-c1dd-35b5-970d-de67551a68f2 | -11.2975 | -53.981 | 2025-05-22 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1f8e14e8-6858-3102-9bfd-6a7b9951d120 | -17.34423 | -51.90157 | 2025-05-22 04:46:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ca330bd-2dce-32d8-9569-498b251a4cec | -14.03396 | -55.13657 | 2025-05-22 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 702d526b-dc98-3225-bc91-ac4e669be5e1 | -13.78419 | -54.30905 | 2025-05-22 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b70508cb-0d76-393e-9eeb-59beab81b198 | -11.11461 | -54.66362 | 2025-05-22 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e9c0b62a-471c-34f8-83ee-fb75b0477012 | -11.6671 | -54.93839 | 2025-05-22 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77f20f1d-3cb5-3a79-9b73-81b586550e4b | -13.47459 | -52.27672 | 2025-05-22 04:46:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc3943be-5a91-35cd-a85d-487a7ba2948a | -12.30113 | -52.48402 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57123279-de2d-3aef-a314-d17b4e17c89a | -12.84599 | -47.39104 | 2025-05-22 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48194534-8429-3acc-9521-b812d0889a69 | -10.70371 | -59.12183 | 2025-05-22 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e6ecbf4-791f-3f87-a97b-dd5490a9ad62 | -14.02571 | -55.1432 | 2025-05-22 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6703377a-1278-3612-9f97-196d89a89cc4 | -11.08192 | -54.77281 | 2025-05-22 04:46:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71cecb15-df65-32e3-8809-cd5993b3514b | -12.34945 | -49.97595 | 2025-05-22 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 27f13852-dcd7-3971-86d2-7a4540b6f4c1 | -17.15331 | -54.01034 | 2025-05-22 04:46:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f6e83f21-b7e8-37d1-924e-0cc079866c2a | -13.06625 | -52.0219 | 2025-05-22 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21e781b1-751a-3dd0-a679-645a003f45c4 | -12.48853 | -57.18319 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9081e0e8-6525-3c8c-92ef-4711febb2145 | -11.12867 | -58.61433 | 2025-05-22 04:46:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e6f3454-208e-310e-ba1e-9dda9af4e28c | -11.11878 | -54.66024 | 2025-05-22 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d185d41d-a9db-399e-a292-8c333f3f594e | -12.28178 | -57.25959 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a7ba869-bf20-3efe-898d-f8f0c7d4db1e | -12.66228 | -58.21957 | 2025-05-22 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a36b75dc-28a6-389b-ba49-2cdf958596ae | -13.4932 | -55.66277 | 2025-05-22 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09016dbf-4fa4-3af1-b196-b35b91cbd98b | -13.53141 | -43.67683 | 2025-05-22 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7bf3e044-08c6-3a14-b8e0-3760ae27bd95 | -14.0339 | -53.3768 | 2025-05-22 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecee8f58-2acc-30b6-92de-233e369a0df4 | -12.34249 | -49.97485 | 2025-05-22 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b1a6063-2414-3677-b9d6-d3ead2f4f4ce | -13.66605 | -53.93346 | 2025-05-22 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 518f8e74-179c-333e-b018-de6a53918f06 | -12.50758 | -57.21334 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 940f86b5-b65d-3fb2-bbd4-62cdf6d7a653 | -13.6145 | -55.45793 | 2025-05-22 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9b0838d-7858-36c1-ac0c-5402d971ad4c | -12.33901 | -49.9743 | 2025-05-22 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d5de0ce-9e8e-3292-946e-b6f925db6d93 | -13.78141 | -54.30476 | 2025-05-22 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0eba5e7e-7403-378e-8cb4-677693d2f3d8 | -12.3011 | -52.5057 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d28f9e73-ce2a-3d7a-b437-9e6026d0feaf | -12.11149 | -49.29718 | 2025-05-22 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32b4bbf6-1cd1-3577-b863-aad50a5467b2 | -13.53159 | -43.6812 | 2025-05-22 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 577c9d81-cb29-3b5a-9464-2de206ab692b | -11.91818 | -54.40954 | 2025-05-22 04:46:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a05fe92-ba1e-3fa8-92f3-d5cfe4b77d03 | -12.13067 | -54.65556 | 2025-05-22 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ec5309b-4e9f-3085-b89c-3929c9d4e60d | -14.03001 | -53.37982 | 2025-05-22 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fb455cd-37ee-34ba-bdc4-f5ff101b1e7a | -12.27688 | -57.2641 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d6556e05-6341-3682-b687-f65693c43834 | -13.66269 | -53.93287 | 2025-05-22 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16b39229-779d-3f2c-8144-81c9a5c14689 | -12.48095 | -57.18623 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8879823-ffb0-35cf-862c-5ac10a7ddbf6 | -12.35677 | -49.98417 | 2025-05-22 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e87b42a9-8832-3839-8fc4-3979c6074722 | -14.03665 | -53.38093 | 2025-05-22 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9d9c8b34-4af1-3bd9-91d9-0d40fdb5da33 | -13.7808 | -54.30848 | 2025-05-22 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0d3bddbb-c625-300c-a06e-25929464da80 | -11.08125 | -54.77681 | 2025-05-22 04:46:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8054b9a8-3ba8-3416-84aa-0a8372d718cc | -17.61248 | -54.17441 | 2025-05-22 04:46:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4b0d2734-b1d6-3b3c-9c75-43c447789247 | -11.07772 | -54.77622 | 2025-05-22 04:46:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 361aa987-c960-3174-b1f7-1b67173805e3 | -12.66646 | -58.22039 | 2025-05-22 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0945048c-8fa6-36c9-ab7e-f2659969459a | -11.08058 | -54.78082 | 2025-05-22 04:46:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README19.md)
