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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65f21def-2744-3c5b-95e1-b279c515b998 | -2.4636 | -49.2089 | 2026-09-20 01:10:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| d170e965-5822-399d-b1b9-146ebdf678ee | -11.0802 | -54.0302 | 2026-09-20 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| ec780661-79ee-342c-8d44-36a168cd370e | -8.1872 | -54.7622 | 2026-09-20 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 5faef509-20e6-3972-bf51-ee5d62aa8d92 | -8.1686 | -54.7634 | 2026-09-20 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| ba11878e-2158-308e-9c54-e9271489797c | -11.1369 | -54.0251 | 2026-09-20 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 588df272-45d0-35b3-a9be-fd58ec0f56f1 | -6.1653 | -47.5052 | 2026-09-20 01:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 23ed590a-1c5b-367c-881f-a90d21bc98a5 | -11.8735 | -47.6793 | 2026-09-20 01:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d5fa1c80-93f4-3c51-8d2f-4f7e7321c757 | -11.8682 | -46.8529 | 2026-09-20 01:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 05ac8a44-d4e9-348e-b07c-1e91eb98e498 | -7.5525 | -45.4123 | 2026-09-20 01:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 5d696b89-71ec-3f93-a7c2-2a412b50fbb8 | -11.8739 | -47.657 | 2026-09-20 01:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 96070265-1746-3f09-8c12-73a4b8242849 | -6.295 | -47.6055 | 2026-09-20 01:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| ead37557-f453-3c38-bab7-528e78db3e23 | -12.74 | -46.18 | 2026-09-20 01:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8e78f115-3998-35b7-bb54-d3d797df4973 | -11.4537 | -45.3892 | 2026-09-20 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 3e05a853-a529-3756-9359-78bd8fb583dc | -3.3367 | -57.8673 | 2026-09-20 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 894ebd12-48e0-3a23-92a1-21be6d6fd3b6 | -7.5525 | -45.4123 | 2026-09-20 01:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| dc3a34c5-f2ed-365e-8aa6-4011fe81a3ce | -5.8595 | -53.5196 | 2026-09-20 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 79359ab5-f0ef-34a7-a0e2-5a71b52134f0 | -12.5419 | -50.0243 | 2026-09-20 01:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| ba349a6e-165e-30b3-aef0-ef856c3b17a4 | -7.5284 | -45.8885 | 2026-09-20 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 066555f2-303d-3e7d-9d58-77c45832de07 | -11.8487 | -46.8781 | 2026-09-20 01:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| cde0c6c3-3f9b-37a0-96d3-90acefda68c3 | -3.7453 | -51.8288 | 2026-09-20 01:20:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 5f52dd5c-1da6-348b-b3b0-1574fd106229 | -8.1872 | -54.7622 | 2026-09-20 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 58e6aa52-1e05-3dde-9a09-5e9c343c1274 | -5.841 | -53.5205 | 2026-09-20 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 82258e8b-9507-33fb-bf2c-3d661b16e17f | -12.7616 | -46.2029 | 2026-09-20 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| e6a60eec-1091-327e-be52-72e4975785b7 | -7.326 | -55.5953 | 2026-09-20 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 1971f01e-31ce-3888-87d2-3b56bcd4773f | -11.0802 | -54.0302 | 2026-09-20 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 0f2c140b-57db-3ba2-b03f-9686432a7502 | -11.8491 | -46.8556 | 2026-09-20 01:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| e882feff-126d-341c-9d6b-8c5b9020e85a | -7.5522 | -45.435 | 2026-09-20 01:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 4c3411a8-caad-3488-9f4e-8b275a354ce2 | -2.4636 | -49.2089 | 2026-09-20 01:20:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 03836162-b6d5-36f1-b860-1c2d73fbfde2 | -14.6856 | -46.6886 | 2026-09-20 01:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 3e667068-a77d-3d8f-9353-30deed31ad32 | -15.2288 | -53.8481 | 2026-09-20 01:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 643c1eeb-7c82-35fb-9abb-323f99369369 | -9.131 | -45.7273 | 2026-09-20 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 52f8e7d2-0c15-3998-b48e-0d1acd9a22e1 | -8.7911 | -60.7935 | 2026-09-20 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| c0a14027-cf6b-365f-985a-76fcb4fc7304 | -8.1688 | -54.7432 | 2026-09-20 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| a300e4f7-e46a-3d01-b0f8-68fbebb7a100 | -3.6945 | -60.6215 | 2026-09-20 01:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| e4a27315-e9b1-34da-a481-a74af289c2e4 | -3.6946 | -60.6025 | 2026-09-20 01:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 42530da5-fcc6-3701-92ee-59fce1d1107c | -15.2284 | -53.8691 | 2026-09-20 01:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 19b5cc56-4180-3238-ab5b-57fdf5ee09e0 | -10.4107 | -48.8894 | 2026-09-20 01:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| e7e8f0f5-150e-363a-adb4-25e15c6bdec0 | -11.118 | -54.0268 | 2026-09-20 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 2342c14e-8b58-3a05-8dd4-02631364c6af | -8.1686 | -54.7634 | 2026-09-20 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| a482e3de-069c-38ed-8d11-00c0cce446cc | -13.0177 | -46.9125 | 2026-09-20 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 74683fd0-fbe1-31e1-b69f-2d90c3404689 | -5.8593 | -53.5399 | 2026-09-20 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| af037e95-c161-3e78-b9d8-27cd6861e981 | -11.8679 | -46.8755 | 2026-09-20 01:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 58571db9-dc42-3ba9-adc7-177ed4f027f7 | -11.8739 | -47.657 | 2026-09-20 01:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 16e86f6b-477a-3d72-89ad-1d470b942ed1 | -5.8408 | -53.5408 | 2026-09-20 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| e73f62bd-38da-37c2-b1ca-bc6c4ce855b6 | -10.4103 | -48.9112 | 2026-09-20 01:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| de00aae1-68f2-392a-b9a9-ae68192368aa | -10.3917 | -48.8915 | 2026-09-20 01:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 144.1 |
| e4945b5b-876f-30f7-afa5-037ab8db67ed | -10.3914 | -48.9133 | 2026-09-20 01:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| ee7df1bf-69dd-3d9f-a124-27aff107e32a | -11.2307 | -54.078 | 2026-09-20 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 875438e6-400a-32e2-bdfd-3915133b25df | -11.2118 | -54.0797 | 2026-09-20 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| c4f1b238-ce6e-3803-9da8-7ad5709c9fe4 | -3.7454 | -51.8082 | 2026-09-20 01:20:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 879d062d-0ddd-366b-be95-cccf1a243cc0 | -6.1653 | -47.5052 | 2026-09-20 01:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 457b1e0a-4b08-3588-92ca-a24bfd04510f | -2.8791 | -57.799 | 2026-09-20 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| a825bc28-d89e-3c97-b30d-7b23b6efeff7 | -13.037 | -46.9096 | 2026-09-20 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| dcee613d-fbb4-3cd6-b58c-c089dd3193ff | -2.8791 | -57.8184 | 2026-09-20 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| abefa85c-fd1a-36b8-bca9-c38db49809b0 | -7.5472 | -45.8868 | 2026-09-20 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| fc8b5847-22de-3d31-8073-86af1116b577 | -7.3259 | -55.6153 | 2026-09-20 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 82f724d0-bb17-32e9-ac8c-63ba37449f18 | -11.0991 | -54.0285 | 2026-09-20 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 478dbef6-dd34-3cc0-a6e6-e68ea0a7adad | -2.4451 | -49.2093 | 2026-09-20 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| efc7c691-1bcf-3cdc-93e6-95713109e119 | -11.2309 | -54.0575 | 2026-09-20 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 130481ec-54ed-3378-aabc-555cd78f89de | -2.8974 | -57.8181 | 2026-09-20 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 51dc8bbd-e80b-336f-9455-020aed9e0f77 | -11.8547 | -47.6596 | 2026-09-20 01:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 21dd1d06-7844-366a-a6b2-071c0237c776 | -9.94182 | -60.73337 | 2026-09-20 01:20:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 71af91cb-ea65-3c3e-8cfc-1b2ec7c81c5e | -9.54915 | -66.03045 | 2026-09-20 01:20:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d24f6737-3c3d-3678-b49a-140ee731132a | -10.5679 | -68.66645 | 2026-09-20 01:20:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0ec70f8f-e77e-35bb-ba61-e519f7bbc0e5 | -10.0665 | -67.8411 | 2026-09-20 01:20:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7959293f-0608-325b-b07c-abd8a156689b | -9.54758 | -66.01967 | 2026-09-20 01:20:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 97d59549-7595-3b45-a086-6e84b2d071ef | -9.67313 | -66.82259 | 2026-09-20 01:20:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0965faca-43d5-3c1c-9348-f59b815501eb | -10.56912 | -68.67535 | 2026-09-20 01:20:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 69efd19f-bcb9-32da-9623-94652cdce6a8 | -9.55725 | -66.01817 | 2026-09-20 01:20:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 222dba3a-858c-38e8-89f7-ba1aafcb40f8 | -7.61836 | -73.09501 | 2026-09-20 01:20:00 | TERRA_M-M | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 920dd890-73a5-36ba-89ac-71755d31f558 | -9.05753 | -69.61866 | 2026-09-20 01:20:00 | TERRA_M-M | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0d16ee3b-3d21-303e-9168-40a71106d77c | -6.93908 | -62.92094 | 2026-09-20 01:20:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| c7bac684-e850-30bb-b7a7-bbd36d3a8936 | -7.04981 | -62.95767 | 2026-09-20 01:20:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| f34b9cbc-81b1-35e9-a4d5-32ec23ef5fd3 | -7.61997 | -73.10768 | 2026-09-20 01:20:00 | TERRA_M-M | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a8986f46-3020-3acd-a6d8-bdde29ef85f9 | -3.67947 | -60.5971 | 2026-09-20 01:22:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 593b0741-cd74-33c6-b9cd-dd5c6c88dea6 | -3.68628 | -60.58918 | 2026-09-20 01:22:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 9f31ce9c-0824-3cb5-b2ad-37d243fbc4d9 | -3.11705 | -61.42426 | 2026-09-20 01:22:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 246df222-9635-32f8-be89-560260a4f57b | -3.69576 | -60.59461 | 2026-09-20 01:22:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 4e4c07b6-3e31-3523-86c4-fc0145d79181 | -3.69174 | -60.62376 | 2026-09-20 01:22:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| c5668dbd-0e52-3e62-a409-a2dc334baa5a | -3.68471 | -60.63178 | 2026-09-20 01:22:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 4830cb8f-7205-3b2d-9734-952359873d73 | -5.8595 | -53.5196 | 2026-09-20 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 9bede7fe-8899-3e3b-b216-ce68c9286695 | -5.841 | -53.5205 | 2026-09-20 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 31348b97-575a-3675-8ff0-ab93d2ea69c6 | -8.1688 | -54.7432 | 2026-09-20 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 0727f56d-9a10-3293-a4ff-11289cc991da | -14.6856 | -46.6886 | 2026-09-20 01:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 87.9 |
| f736a2bd-1a01-35cb-8255-4f3c76432bc5 | -7.3259 | -55.6153 | 2026-09-20 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 74188d2a-ea67-3a3e-8f71-6d093f757810 | -11.4537 | -45.3892 | 2026-09-20 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 5ca93314-3f27-39a8-951e-1a4b8a581452 | -8.1686 | -54.7634 | 2026-09-20 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 7a2ff6e6-60d6-3533-8dbe-aa2aa3b068c0 | -13.037 | -46.9096 | 2026-09-20 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 3998f0f5-28e0-3b5d-91d6-8b4f7a9f91f1 | -3.6946 | -60.6025 | 2026-09-20 01:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| a2a39f83-8802-3354-93d9-151b8e4ebeb8 | -11.0802 | -54.0302 | 2026-09-20 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 9c0d4433-b267-38e0-be4b-566c411d79f0 | -11.118 | -54.0268 | 2026-09-20 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 6a446616-1cf4-3d01-8f7a-c1dbcea879f1 | -7.5284 | -45.8885 | 2026-09-20 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 2f3a742f-1d99-3dcc-834c-0fe8625c2ea5 | -11.8547 | -47.6596 | 2026-09-20 01:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 48d5610b-b579-3467-a1ba-1b0f3635d9bc | -2.8974 | -57.8181 | 2026-09-20 01:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 5cc17087-ae11-3d15-a7e4-d10273169044 | -3.7453 | -51.8288 | 2026-09-20 01:30:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 1a33c027-c37c-343c-9c4e-97967433dc50 | -11.8487 | -46.8781 | 2026-09-20 01:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 0871932e-fd06-3cca-8fbb-25ed74a645b6 | -7.4286 | -44.7409 | 2026-09-20 01:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 61.0 |
| ccbc94d6-8041-3632-8375-781abb321fce | -7.5525 | -45.4123 | 2026-09-20 01:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 124.9 |
| d7121d7a-e63a-394f-ab11-768b5b25bcc5 | -7.3073 | -55.6163 | 2026-09-20 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 5c8b1c8a-4533-3505-8823-e8c9ffe99a27 | -8.1874 | -54.742 | 2026-09-20 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |


[Clique aqui para ver as próximas entradas](README6.md)
