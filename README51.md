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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 164bb775-9cf0-3fc4-9224-f7fafa2776cf | -15.2882 | -56.42859 | 2026-08-18 04:59:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 194dde29-8c92-303b-8d29-b96e5fb8a7cf | -14.18182 | -52.93547 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98b6f898-f84a-3ff4-8d86-7194268b521e | -16.227 | -57.6571 | 2026-08-18 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 050567d1-73fd-319f-9672-28b94ee7d20d | -15.88035 | -55.55364 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 538373ec-0c77-3e7e-ac43-4280c566f028 | -14.16711 | -52.895 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b3149da-2ba3-3cf8-87db-361d10e2363a | -14.18522 | -52.93599 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53ff8c4b-6133-382f-b7c8-bbe1062961c8 | -14.16089 | -52.91307 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 825c4eb9-b592-3bf6-956c-e87dcbf6140c | -14.18466 | -52.9397 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 480c156c-0a16-3b4f-bbb9-5ec0af7f7b59 | -14.39214 | -53.30502 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 672b9e50-20d6-396d-a3ad-453c317e5f17 | -16.74367 | -50.22118 | 2026-08-18 04:59:00 | NOAA-20 | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f28f51d3-8d96-35f8-9554-498c57889df8 | -13.42633 | -57.07626 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5f7e703-25b9-3bb7-bcae-327e7d0cbdf4 | -14.81367 | -46.63717 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7491060c-22c7-31dd-aedc-31e2d7506ab0 | -14.17381 | -53.05606 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f812ecf1-4c86-3fa9-812a-76ccfe178af0 | -14.25978 | -51.93946 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5cc6d94-8c43-3416-af4d-c517ea95b489 | -14.8228 | -46.6419 | 2026-08-18 05:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 89.0 |
| f67e220d-7a1e-3155-82ca-3e0f39a3a9d3 | -6.841 | -59.0132 | 2026-08-18 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| e79c3889-8b25-34df-b9dd-270df3520ba7 | -8.222 | -55.0418 | 2026-08-18 05:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 8ad00be6-5fe4-3547-ab71-7941fb4b0dd0 | -9.0673 | -50.8419 | 2026-08-18 05:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| adb749b1-5594-390a-a219-b86413169e93 | -6.7478 | -59.1716 | 2026-08-18 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 858b6e35-a5d2-3c0d-b6d6-f0311dc41426 | -6.8594 | -59.0125 | 2026-08-18 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.6 |
| c7fcd1ea-4f18-3140-a096-f77738170657 | -21.72206 | -49.76046 | 2026-08-18 05:01:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 0dd2320d-bd55-358f-878c-e06db9d806cc | -22.57388 | -48.56049 | 2026-08-18 05:01:00 | NOAA-20 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 08bfaa85-dfb0-3852-a443-644ce57a5ba9 | -22.06733 | -55.98727 | 2026-08-18 05:01:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8f20b265-96fc-3b2e-8fae-88a5351eed6d | -22.07065 | -55.98787 | 2026-08-18 05:01:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1e52bc87-5294-3558-b3f6-d79e676a21b9 | -20.59127 | -45.9305 | 2026-08-18 05:01:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c08f463b-3043-3feb-99c6-08d50d5d73a7 | -21.61818 | -49.01697 | 2026-08-18 05:01:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9f3745b-0526-3a4c-8d50-b0da711e5ef8 | -23.53728 | -47.29783 | 2026-08-18 05:01:00 | NOAA-20 | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8e765f16-c1e4-3fef-b987-afadeaa075f2 | -20.59192 | -45.92387 | 2026-08-18 05:01:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d401c9f-9ddc-3b49-bd42-c08d134970bd | -21.75554 | -48.80101 | 2026-08-18 05:01:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81207829-ee4b-37d8-bdc5-04bbebaf5cd8 | -23.62009 | -51.78404 | 2026-08-18 05:01:00 | NOAA-20 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 79fe9e94-ab8c-3f48-bea3-2c9fb25a8aa1 | -22.06401 | -55.98666 | 2026-08-18 05:01:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aa2c092e-aa09-3d88-a229-b65306b16d29 | -22.0695 | -55.99529 | 2026-08-18 05:01:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71437e5f-0663-3deb-9f7a-205a84d2d878 | -22.06184 | -55.97865 | 2026-08-18 05:01:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05f19a8d-db0c-3bc5-8368-d412fd204461 | -20.83637 | -57.67276 | 2026-08-18 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| be3855e5-7adc-3a4b-aef7-ca84a762cacf | -20.59658 | -45.93354 | 2026-08-18 05:01:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b4d1ff0-8f38-3b6a-88cb-c962970afbb9 | -20.64076 | -57.93512 | 2026-08-18 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 956da456-2a83-3b24-87d1-42565d859eeb | -22.06019 | -52.18876 | 2026-08-18 05:01:00 | NOAA-20 | MARABÁ PAULISTA | SÃO PAULO | Brasil | 3528700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3a395730-b290-38b8-bbd4-66710fa28374 | -22.06286 | -55.99411 | 2026-08-18 05:01:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2f4ab40f-84de-3d53-90f9-99ff02512408 | -21.7584 | -48.79839 | 2026-08-18 05:01:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91d19b47-2d89-3744-bd0b-4f8b03038deb | -21.61762 | -49.0221 | 2026-08-18 05:01:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f9d0d8f-c903-3e15-8b7a-1c236c814de4 | -22.06618 | -55.9947 | 2026-08-18 05:01:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 548ee42a-c72c-3d19-b73d-a2b0b311fcd6 | -21.04901 | -55.83416 | 2026-08-18 05:01:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df65eb1b-8ce8-377c-9d91-d5ef9c5cd6ae | -22.06086 | -52.18377 | 2026-08-18 05:01:00 | NOAA-20 | MARABÁ PAULISTA | SÃO PAULO | Brasil | 3528700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a9035135-89c5-3599-9138-8d5f4ba3eea7 | -20.62076 | -45.91621 | 2026-08-18 05:01:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bdcbee5-ceab-34fa-8aac-6d5b0a34984f | -21.61843 | -49.02048 | 2026-08-18 05:01:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a8677a8-1d79-3524-a7b1-ad3aaf9b30d1 | -23.53695 | -47.30132 | 2026-08-18 05:01:00 | NOAA-20 | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ddcbcfe7-5934-375e-90c2-4ca80ecfb162 | -20.62706 | -57.91245 | 2026-08-18 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 8ed25ab2-a797-3b7e-9b2e-b31d8bfccee5 | -20.63659 | -57.91828 | 2026-08-18 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3f742822-3313-37b9-99a5-22867f8a6a68 | -20.84038 | -57.66958 | 2026-08-18 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 4cc0b680-0cc2-397b-a3fc-632c1a983846 | -20.6151 | -45.91661 | 2026-08-18 05:01:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c653d981-1194-3450-b0ff-1ff00505174b | -21.61384 | -49.01981 | 2026-08-18 05:01:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2acbb983-e11e-3da1-9476-496cdaa3d53a | -20.83702 | -57.66895 | 2026-08-18 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d9bb03ab-ecad-3cf9-a7c3-6fd7aefd46fd | -20.59158 | -45.92729 | 2026-08-18 05:01:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f993e85-cda4-383f-b5ee-0e3db0e97d4a | -20.59786 | -45.9205 | 2026-08-18 05:01:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c0d224c-9d9b-3dab-bbe6-2a83386141fb | -20.62036 | -45.92017 | 2026-08-18 05:01:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95cb8329-8660-38a0-b57e-0f80e04c3a12 | -23.8222 | -48.70871 | 2026-08-18 05:01:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3dd62c6d-832d-389f-87f8-d3bb84845329 | -21.97347 | -54.64491 | 2026-08-18 05:01:00 | NOAA-20 | ITAPORÃ | MATO GROSSO DO SUL | Brasil | 5004502 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 984b88d3-52c1-3864-84e0-a3e82f153d18 | -22.06126 | -55.98236 | 2026-08-18 05:01:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 812618f7-09d9-363a-833c-92e17c23c6a9 | -20.64063 | -57.91505 | 2026-08-18 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 23720f75-ca67-3c1a-b965-9a08e36c49a0 | -22.07398 | -55.98845 | 2026-08-18 05:01:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c5c22439-a517-3526-9659-a53142c27a40 | -22.07008 | -55.99158 | 2026-08-18 05:01:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6551ceac-3196-394e-89e6-744dceb48eaa | -23.1899 | -49.1582 | 2026-08-18 05:01:00 | NOAA-20 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6d13a82c-43be-3e0b-a5b3-7f2d98b2603d | -23.68406 | -51.67641 | 2026-08-18 05:01:00 | NOAA-20 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a2ba97bb-b852-3ed7-9d73-0ac4a4d3e755 | -8.604 | -50.3527 | 2026-08-18 05:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 7f3d9f38-7045-370a-8245-184d202fabfe | -14.1821 | -52.93 | 2026-08-18 05:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 140.2 |
| d77affd2-fdf4-3c8c-9cc3-b62e5421d280 | -6.841 | -59.0132 | 2026-08-18 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 557ed750-ad63-3114-806b-75b1c8a0241e | -14.1828 | -52.8878 | 2026-08-18 05:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 0d6de3b6-32c2-393c-adde-d0bc80a2b32c | -14.8228 | -46.6419 | 2026-08-18 05:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 56102bb0-8f5a-3334-84f8-766867152a82 | -6.7478 | -59.1716 | 2026-08-18 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| d9ff2540-4bc8-323b-918e-25467518bc7e | -6.8594 | -59.0125 | 2026-08-18 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.8 |
| d4457e8d-8afc-3905-bb00-e58d68e5ad16 | -6.7663 | -59.1708 | 2026-08-18 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 2c491286-6875-30f3-b232-48423711e823 | -14.1824 | -52.9089 | 2026-08-18 05:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 185.9 |
| 5e3cdb08-528b-3711-a9b1-4d038e6ecc8f | -14.1628 | -52.9323 | 2026-08-18 05:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 4fc2e168-8a3e-3b07-b7cd-431da2d497f7 | -14.8233 | -46.619 | 2026-08-18 05:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 85904b7c-be41-3452-8cad-f159df66e4c5 | -14.8033 | -46.6453 | 2026-08-18 05:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 69.5 |
| e93ce312-05d1-3377-8127-e4a7b39ae1f8 | -8.222 | -55.0418 | 2026-08-18 05:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 84cdd3e5-ab2c-3212-847a-2d063d055fac | -14.1631 | -52.9113 | 2026-08-18 05:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 21a5e8ff-dcf2-3c30-8bd5-0c87684bee95 | -8.57 | -54.73 | 2026-08-18 05:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3d12858-e82f-3259-9b4c-bd4bafbb0eaa | -14.19 | -52.93 | 2026-08-18 05:15:00 | MSG-03 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ad58130e-f59e-3c0b-8918-08a0d4cce2f2 | -8.6 | -54.74 | 2026-08-18 05:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a082edbf-ceee-36a2-aa87-d46ca00b5e16 | -9.0673 | -50.8419 | 2026-08-18 05:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 3bb25285-51f2-3f7b-a1b6-076bc5707b2f | -14.1628 | -52.9323 | 2026-08-18 05:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 0b01954b-8a63-3f98-809c-5be2d4ceeba0 | -14.8228 | -46.6419 | 2026-08-18 05:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 795248dc-319c-3b4a-85c1-789b4f1a4fd7 | -14.1631 | -52.9113 | 2026-08-18 05:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 6f1f3e41-0d48-33a6-b1dd-3426ad2f75bf | -6.7663 | -59.1708 | 2026-08-18 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| db787885-0259-30bc-95d9-220bf8976f4d | -6.8594 | -59.0125 | 2026-08-18 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.4 |
| b09ddccb-c9b4-3b8d-9eeb-b470695ac3e2 | -6.7478 | -59.1716 | 2026-08-18 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 211ba629-b6d0-3575-a6db-c608d34fd06e | -6.841 | -59.0132 | 2026-08-18 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 88bc5191-62d9-3d07-9895-68de80175cee | -14.1824 | -52.9089 | 2026-08-18 05:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 4c55e02a-b53c-32cf-ba59-2fae58106712 | -8.222 | -55.0418 | 2026-08-18 05:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 505eebd4-b1d3-3131-9483-4f810b61da58 | -14.1821 | -52.93 | 2026-08-18 05:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 132.0 |
| a3a706cb-dae2-375b-ba3a-be5423676401 | -14.1828 | -52.8878 | 2026-08-18 05:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 82a1ae2c-67dd-3a9a-9427-32d8c44bd21b | -9.0673 | -50.8419 | 2026-08-18 05:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 1082e2d0-85f7-33e9-a7e5-1c9d56c96963 | -8.604 | -50.3527 | 2026-08-18 05:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 1d8a11bc-330a-3dec-affa-91bf13ba69ef | -14.1821 | -52.93 | 2026-08-18 05:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 159.4 |
| d6cc1cff-6f32-3e12-9132-98aef80845d6 | -8.222 | -55.0418 | 2026-08-18 05:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| f3f9d01c-b180-3605-870d-e2a22a3fa080 | -14.2017 | -52.9065 | 2026-08-18 05:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 286a9a71-1a37-3d2b-90db-6d98664a6ce6 | -14.1631 | -52.9113 | 2026-08-18 05:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 66773791-b046-3ca3-94bc-679563186676 | -6.841 | -59.0132 | 2026-08-18 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 68d0784a-0ba1-3046-8038-2877fa8b7a6c | -14.1824 | -52.9089 | 2026-08-18 05:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 230.5 |


[Clique aqui para ver as próximas entradas](README52.md)
