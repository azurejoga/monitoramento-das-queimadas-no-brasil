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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0aee6faf-0366-3969-8ab5-5b1bd74965fb | -12.76412 | -47.96835 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fd92f0b7-a401-302f-a6e7-93c97ffe5003 | -12.96132 | -47.96088 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 094795dc-be16-3145-9297-81733c40509f | -11.70261 | -46.8685 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ece160e2-3199-3f5b-9220-0f8da64cc9c7 | -11.04765 | -48.26804 | 2025-09-16 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb4607dd-8377-3b9e-a1d1-01fa292ddd7c | -12.05334 | -46.53173 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad63a63b-1972-35cc-9c4a-8492bdcfdda6 | -13.19027 | -47.30283 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e52c65d-11cb-3d81-9eae-0e2c67a6d86c | -8.91065 | -46.15206 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd072e0a-159d-3375-b76e-bf1823706c5a | -12.79156 | -47.26067 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fe68a804-c1ca-3bef-9a0f-b4ef321a7064 | -7.71179 | -45.30744 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5025f052-49bc-31de-b73f-3e7b05e208d5 | -7.71417 | -44.81947 | 2025-09-16 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25ba80d6-076e-3da0-93a3-720e908ef71a | -8.96332 | -46.03376 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4661fed5-3ca4-361e-8943-d3556efa17d1 | -12.62523 | -45.77407 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0bffc7da-cab5-39da-8fbf-8ab0a3a683a5 | -11.70933 | -46.89123 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1198a09f-c751-3222-aa9e-bf11f247d930 | -12.61266 | -47.98381 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6cd51a5-6935-3403-af0a-548917504e18 | -7.40302 | -50.00412 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| da184a79-8031-3b20-b758-89a1a85e16cb | -8.3089 | -45.64071 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fa31bc8-e12f-3ef8-8d2e-da98f40a8256 | -12.83793 | -47.21671 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80d8a7cb-e19c-38fd-b322-71d53e9cd809 | -13.06217 | -50.08358 | 2025-09-16 04:29:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67395b54-524c-392e-93d2-542d01ab7784 | -10.87182 | -45.43799 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c6421c8-1bf7-318b-a53b-c2aa71e5b14d | -9.06933 | -50.30636 | 2025-09-16 04:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 241b0015-c44e-3d65-8324-cd2f6bad0029 | -9.23488 | -45.67725 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa12d819-04a0-3eab-8b7c-5cd576ce9842 | -8.00013 | -43.83358 | 2025-09-16 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 627e5c08-961a-347a-b74e-ae6fea4fe3d6 | -12.76468 | -47.96482 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa9ed930-5461-3b98-9df5-391447bb5257 | -9.54032 | -46.29802 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 931cf0c8-3318-39f6-8c6b-086076708f8c | -8.9101 | -46.15558 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7822b6c0-e87e-366b-b07d-b70015a1573f | -10.72371 | -44.74456 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c715eb5-b1bd-37f0-a23b-df84f191ed7a | -7.53222 | -46.72532 | 2025-09-16 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fd02ead-f9ae-3816-9bc1-b0f40704d15f | -13.21303 | -47.28846 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e75006b8-d2bf-328d-80b7-c5bef3043732 | -12.80545 | -47.23745 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2a59228-8b97-3055-81b3-1f5ac9d86d73 | -11.99367 | -46.67294 | 2025-09-16 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66e16ac9-de49-3ff2-9256-7ffb2f6d41a8 | -12.6848 | -48.00298 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ab52f37-6857-3bdf-a905-988dcf524c4e | -9.09676 | -44.846 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 835684d4-fc15-3ab9-b104-ab0b762a33c7 | -7.99193 | -45.66835 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 137e7461-486f-32fa-a644-eedc863eb15d | -12.11894 | -44.83995 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f47e35f1-bde4-3f78-97c3-e21185ccf566 | -11.50393 | -43.73264 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 825f90c0-cbae-3154-961d-74aac8545402 | -11.70599 | -46.8907 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1a43a3d-5122-3129-b5e2-d2ae7a5dde3b | -11.70544 | -46.89424 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd80ca71-ff37-3027-ad75-6155ae9643ea | -11.13347 | -45.34604 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 797662a7-6a07-3f5b-bf45-8c6e70d6a605 | -10.76384 | -44.71763 | 2025-09-16 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bc0a510-5e2d-3d14-b251-454823c40123 | -10.4709 | -45.16201 | 2025-09-16 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90704b09-fa45-33dd-8103-d854632f3284 | -8.97979 | -46.25687 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 72774378-4687-3a7e-98f6-7b892b9c970c | -7.93636 | -47.65099 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 136e9bce-31b5-38c4-a560-aea66905e3c7 | -12.65811 | -47.71878 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ff6471a1-de83-3c3b-bc88-128388b7c5d7 | -11.27921 | -45.30576 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e682564-8063-3cb3-9381-ef1e10daf67c | -11.12543 | -45.30584 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a122258-c65b-3dd3-8af2-1485812269fb | -10.71379 | -44.73882 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ba2de8de-c44e-34b4-a22f-76c6b3163646 | -12.69095 | -47.98578 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e2e8dd3b-cbf3-3ea0-8ed1-189c42ee180a | -11.12829 | -45.33365 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f33c1abf-1747-35c9-a77f-1d8413c984b2 | -12.67327 | -47.94651 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8e6d8f59-20a8-3038-86e1-df3152e3cfdc | -12.67809 | -48.02372 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| afe54e51-b5cd-38e4-a342-69c00f3c1ff1 | -10.17739 | -46.14336 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| dffe43cc-6652-36db-9c60-e167ade61ed5 | -7.8384 | -43.86005 | 2025-09-16 04:29:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cdd56c36-e54b-335e-a7b6-712cfff71785 | -13.23185 | -40.944 | 2025-09-16 04:29:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7a09e3c6-795b-3f0c-8419-4a1187b8df33 | -13.87818 | -44.85271 | 2025-09-16 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7b10156-c84d-3798-960e-42f33dbfc9d5 | -10.72054 | -44.76708 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be0a38c1-591e-30b0-abd8-8eaac9ef5786 | -9.09795 | -44.86151 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 5b3830a8-6793-32ea-b011-00daee0195cb | -11.27929 | -50.79891 | 2025-09-16 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c8cc4ee-b8a2-34ae-b9c2-592133c2464a | -8.91362 | -45.52446 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87643137-e43e-3d53-bb5c-7e0b276c3549 | -10.95848 | -49.57417 | 2025-09-16 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb413d1a-1b98-312f-ba71-80b25a421891 | -12.62485 | -47.9931 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 409b5391-66b9-3b25-854a-21789546ef37 | -7.83445 | -46.11567 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 139a6688-8e6e-3ed7-810b-d532712ebdc6 | -10.03307 | -45.29314 | 2025-09-16 04:29:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc746f34-628c-3bf1-8f7e-63d1a25caa1d | -7.55981 | -50.45967 | 2025-09-16 04:29:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59d3a577-1913-352e-98a3-f8f6f7c90e03 | -8.11602 | -48.2696 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 12a2c1fd-c16e-3dc3-ab37-61e89cbc9b27 | -12.79093 | -44.74176 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a4c7491-bd8a-3676-b10b-c11706a7478e | -13.93999 | -44.78405 | 2025-09-16 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cdc3ea8-5143-3c85-ac24-38c0f76e9961 | -11.96428 | -48.68827 | 2025-09-16 04:29:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a226ef3a-1881-3ea8-95f1-8e921af2be00 | -8.58806 | -49.87379 | 2025-09-16 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d7c6af2-8969-3178-8539-8be1a65a0fb7 | -10.64115 | -46.46022 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6cd2f7a-42ff-3444-b619-c942537d748b | -8.97505 | -45.75872 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4e62418-3bc0-3fcb-9369-965c8d1c02fc | -12.61051 | -47.95437 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ec83036-f1ec-384f-b5d4-23bbe61d9d14 | -11.70928 | -46.8696 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e41ddcff-06b2-305c-ad50-561ebda4148a | -10.71917 | -46.50138 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 34505a57-9160-3fdb-914f-80edb89ce890 | -11.9637 | -48.69189 | 2025-09-16 04:29:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4bf843c-feac-36e2-9190-9fdbf5522a68 | -12.73486 | -47.20766 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1115ae11-5588-3ece-87a7-1ad937b3724d | -12.05448 | -46.56876 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fd31018-a8c6-3c64-99c7-ca55f8ff208c | -11.70764 | -46.88011 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b032cd97-a40d-35a3-b6d7-dee45a0e0b6d | -12.11645 | -44.84113 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe65ae5b-952a-3018-88b5-283d70edcf36 | -12.2997 | -46.40398 | 2025-09-16 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de7650a8-37af-3888-ab75-deac41acf189 | -12.93355 | -47.96364 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4370b25f-f298-375c-861e-7144dd253d2f | -8.9336 | -46.22428 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a82bf839-7f14-320a-803d-4e8fc161a23b | -13.03503 | -47.99123 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9a136bc-ddf7-326f-b51d-15d3b8203c31 | -9.10197 | -44.85827 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 0b7e98e0-63c8-334b-a43b-f1d9c897bf99 | -12.11713 | -44.82743 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3dbf59b8-fd78-30c1-bccf-dd9eb0e12346 | -11.46613 | -48.69964 | 2025-09-16 04:29:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c64885a1-926c-34f7-90cb-f5fbf96c0ca4 | -11.1306 | -45.34173 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5a94dcd2-a4c5-3173-a505-cdcf99055f48 | -8.41614 | -45.74508 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07d4f812-c355-3ca1-9b5f-153ee7f6ca9d | -13.21027 | -47.30617 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a3e8a284-72b0-38d2-bda8-cbe30c39ea93 | -9.73522 | -48.12404 | 2025-09-16 04:29:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d57d9ec-40cc-35f6-b25f-e8e5e5a2523a | -8.75936 | -48.80327 | 2025-09-16 04:29:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe9e98dc-2f9a-38b8-a3e4-48e99f999444 | -9.0472 | -44.83497 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 17f44700-583a-3e04-8c66-85144a866eca | -11.42984 | -46.93027 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9403efc8-46dc-366b-ab5f-c359f59a5755 | -10.63507 | -48.7397 | 2025-09-16 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6231cfcb-65e3-318e-b835-755cfc339bd5 | -11.43262 | -46.93433 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d17b5b9b-c6e1-37ed-9be1-fc875f2084bc | -10.6456 | -46.45366 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c721e73-039a-3441-9f46-c3317bf4f943 | -9.3673 | -45.38518 | 2025-09-16 04:29:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec8a67c4-7007-36d3-8675-a645df49a781 | -8.97701 | -46.25283 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f257c0e7-84a7-34dd-915b-5e43e8e6ea63 | -10.71784 | -44.75955 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d59e583-c6c7-3d17-8d41-cd17a44f4680 | -7.98563 | -45.65244 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa63f4ef-7f7a-37e2-b4c6-9cd097d1f13c | -11.11679 | -45.31625 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README51.md)
