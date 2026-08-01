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
| 45f40a97-395e-3bb2-838c-f536fd6765a8 | -20.60762 | -57.30863 | 2026-08-01 04:59:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9971e935-58a5-3e6a-b0d1-72e8da902846 | -17.00684 | -48.28506 | 2026-08-01 04:59:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03fbefbd-5bb9-3660-8bf5-05fbff39ff28 | -20.56035 | -57.30803 | 2026-08-01 04:59:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1fdde6b-0735-3c53-8c34-88aa7255b93d | -18.48252 | -51.69748 | 2026-08-01 04:59:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61429ecc-e2d7-3390-b375-471662f5a3a6 | -18.48601 | -51.69801 | 2026-08-01 04:59:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 06495ddb-3cea-3313-9414-7a0f4be5063d | -21.04038 | -55.82561 | 2026-08-01 04:59:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16db4f28-6f84-3b3d-8f2a-73bd8a81679b | -21.25915 | -49.15312 | 2026-08-01 04:59:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7d7af4e3-0ca0-3222-b07f-cab779a78b34 | -20.60979 | -57.29606 | 2026-08-01 04:59:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb06c56a-4691-38f5-b190-2d04e98eed27 | -21.29636 | -56.13946 | 2026-08-01 04:59:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1cd4c648-525a-359a-9573-bdf0c8e00a2a | -20.54454 | -57.25291 | 2026-08-01 04:59:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6a4c5a3-23ba-3c39-a6a8-2e408d0b395d | -20.38376 | -58.02746 | 2026-08-01 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| dcffbfb4-3cc0-343d-b0d2-d9ce81de4999 | -20.3844 | -58.0299 | 2026-08-01 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d063c372-d6df-3bb4-85f4-48cd74d45d96 | -21.24171 | -49.15878 | 2026-08-01 04:59:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| cbc6ea25-3a1c-3541-ba0d-20f2d3897a0d | -20.54806 | -57.25358 | 2026-08-01 04:59:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8252795d-b3fd-381f-864f-3125bb31d0f1 | -21.29572 | -56.14328 | 2026-08-01 04:59:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e70dce9-9470-33eb-a4f5-b7503b056796 | -21.04374 | -55.82625 | 2026-08-01 04:59:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e51cb7a3-d698-3b37-ae3f-958352ae7cd1 | -20.52513 | -51.44124 | 2026-08-01 04:59:00 | NPP-375D | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| faf955f5-419e-3f8c-a837-7033e4180987 | -16.40826 | -53.34873 | 2026-08-01 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eaf0f9e9-9f8e-385a-8dbd-9f18b1a2ec14 | -20.56315 | -57.3129 | 2026-08-01 04:59:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 773d9b91-b6bf-3ec6-a880-373a4f1cdfc5 | -18.48193 | -51.70148 | 2026-08-01 04:59:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d8feee9-6043-3bed-bf63-115242645944 | -17.89556 | -44.30933 | 2026-08-01 04:59:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6029766e-ce4a-392a-828a-b6185db4702e | -20.38912 | -47.74957 | 2026-08-01 04:59:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ceb6b475-585d-3e42-aa08-e8b47bf19463 | -20.5161 | -48.86392 | 2026-08-01 04:59:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 15d7b258-2c49-380a-8623-48b7b58fb0c8 | -17.4244 | -42.62537 | 2026-08-01 04:59:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73cdaa51-6709-30f3-8691-311a63cfe7f8 | -20.54569 | -57.28775 | 2026-08-01 04:59:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e07688b-87b1-319f-b0fe-15495c971d8d | -20.56947 | -57.31843 | 2026-08-01 04:59:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94e6b15e-e3b0-3abd-ac73-fbcffbb8e7bd | -20.11419 | -50.74138 | 2026-08-01 04:59:00 | NPP-375D | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 5e285e1a-525e-311d-aaaa-2a6a799790af | -14.092 | -46.2866 | 2026-08-01 05:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 2ca17d39-c4a2-3ee0-8b8a-73d482cbdae3 | -14.0925 | -46.2637 | 2026-08-01 05:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| b84e33f1-a60e-3c86-b50b-465b0e819a83 | -14.0725 | -46.2899 | 2026-08-01 05:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 551de93e-f30e-37aa-8dfc-f8d2c5361737 | -11.2402 | -54.8534 | 2026-08-01 05:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 60e1c644-2ddc-38d3-a2e4-7c9610b8b7bc | -14.073 | -46.2669 | 2026-08-01 05:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 80aac83f-61cb-304d-b29f-3f9707700d38 | -23.79173 | -49.29303 | 2026-08-01 05:01:00 | NPP-375D | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 82109767-beae-3aa4-b71c-cd7325aeca0f | -21.98277 | -57.60328 | 2026-08-01 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 885fa41a-7f17-362a-86ec-4d3a0764b564 | -28.296 | -49.9837 | 2026-08-01 05:01:00 | NPP-375D | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 03c6784d-3b08-3bcc-a74b-9533f9be54dc | -28.59283 | -50.2352 | 2026-08-01 05:01:00 | NPP-375D | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b4b9be09-3b7a-33e0-9382-a153bdb0ac35 | -28.43772 | -49.57351 | 2026-08-01 05:01:00 | NPP-375D | BOM JARDIM DA SERRA | SANTA CATARINA | Brasil | 4202503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 87130cf6-871c-3e05-985c-c10fc47a460d | -23.78749 | -49.29257 | 2026-08-01 05:01:00 | NPP-375D | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 415ef8ff-119a-3324-add7-341f5fb05c40 | -22.27847 | -55.97775 | 2026-08-01 05:01:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1b06ea4-5fbb-3cba-83ec-3b8b3a2e6ec5 | -21.98234 | -57.60207 | 2026-08-01 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2d06e0f-34d9-340c-8512-9ba59b75405c | -23.02866 | -52.65687 | 2026-08-01 05:01:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 7d135959-3c77-3991-8c4d-51282c05930c | -28.29553 | -49.98806 | 2026-08-01 05:01:00 | NPP-375D | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7d0000f2-d09a-39d9-9635-c38f2db1e272 | -21.98627 | -57.60405 | 2026-08-01 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc164fbd-e7cf-3943-9805-65219ce6341a | -21.98583 | -57.60286 | 2026-08-01 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92d25d27-2129-3778-b3e8-9c99cd7c0b00 | -23.19712 | -49.15512 | 2026-08-01 05:01:00 | NPP-375D | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 283f79c1-f665-3844-8c14-3498a3d64e4a | -22.27639 | -55.96946 | 2026-08-01 05:01:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d38af59-f054-30a8-ac3e-fa90c692c715 | -11.2591 | -54.8517 | 2026-08-01 05:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 62ef2e61-1955-31c9-b66c-2ff18b8490b9 | -14.0925 | -46.2637 | 2026-08-01 05:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 07ebb58b-2f90-3b80-a3ba-48e2d49ffbf0 | -14.073 | -46.2669 | 2026-08-01 05:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 93df3409-2dff-3ba3-bfd1-56a7ab9981fb | -14.0725 | -46.2899 | 2026-08-01 05:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 55.9 |
| ce887d3a-3cef-3e1c-9b93-cbe4d62004ba | -11.2402 | -54.8534 | 2026-08-01 05:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 07963d9f-db29-3530-be43-085e0c182211 | -3.11149 | -47.91671 | 2026-08-01 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b26a2d20-92ed-3372-9a3d-f4d74ad87e12 | -3.84621 | -44.09629 | 2026-08-01 05:14:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8af98113-4f4f-3065-9bf3-eee03b420f89 | -2.88746 | -48.01382 | 2026-08-01 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cc063e3e-8f58-3768-83bd-4a48cbeabe5b | -0.85485 | -52.71587 | 2026-08-01 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f3076dda-312c-300e-8e19-5b3e43c5374b | -3.85297 | -44.0974 | 2026-08-01 05:14:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6785538f-4d83-3b64-b091-c7a1687855c8 | -4.27192 | -48.19475 | 2026-08-01 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7783d1c5-4597-3be8-be5a-13bb0f011ead | -2.81879 | -60.00368 | 2026-08-01 05:14:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a0a8a73-86eb-32fd-8593-66815d5ea701 | -4.61005 | -49.05337 | 2026-08-01 05:14:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1c766408-9422-3a6f-b133-d6fe4ee5d382 | -5.55547 | -43.98045 | 2026-08-01 05:14:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 18598a24-1a7d-31d5-b5fc-2b8a538308ea | -3.11296 | -47.90695 | 2026-08-01 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a6845633-8a16-3e12-8b5a-ed52b2a31fd9 | 1.09801 | -60.50651 | 2026-08-01 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56691e5a-ae0f-3104-8660-a32fe20d3985 | 4.41891 | -60.98314 | 2026-08-01 05:14:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 386c5981-90e6-355a-b420-70ced1ceec30 | -3.85385 | -44.09149 | 2026-08-01 05:14:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c387dbe-bac3-3905-ae76-360a2de1b7ad | 1.09955 | -60.51653 | 2026-08-01 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0239395c-9e31-3d8b-8ab2-de120f598093 | -3.11722 | -47.9143 | 2026-08-01 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9aa91b8a-83eb-35b2-8ea4-e04806fd833c | -3.85474 | -44.0983 | 2026-08-01 05:14:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2407704e-0c0e-3878-848a-45bc5a959f26 | -2.59861 | -47.34431 | 2026-08-01 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2954ffe3-361b-324b-b0be-ef7c20248e28 | -3.05273 | -48.74298 | 2026-08-01 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3f50e8a-cfe1-3615-8666-3f890153c692 | -5.55639 | -43.9739 | 2026-08-01 05:14:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0cb59d98-5b49-3ee2-a8c2-285569ec4608 | -2.16298 | -47.86963 | 2026-08-01 05:14:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd39b526-5fb7-3df0-85b7-df81216fa401 | -2.59914 | -47.34093 | 2026-08-01 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acc6a36e-6d9e-3178-b315-2acd3756d6f3 | -4.61504 | -49.05399 | 2026-08-01 05:14:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5ea909b0-5f56-353b-ba52-4e62fee98489 | 1.09639 | -60.52218 | 2026-08-01 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 538cad6e-8f66-38fb-a8aa-241a6c81cf3d | -5.5573 | -43.96752 | 2026-08-01 05:14:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d0827c6a-ff9b-3dca-b57e-fb7c4d3b276d | -4.36501 | -47.76748 | 2026-08-01 05:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 00e11942-8e0d-327a-9e83-3be6a7addf3c | -2.88698 | -48.01697 | 2026-08-01 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 85a2395b-fb11-3972-9712-7525e08a63f5 | -3.84883 | -44.09122 | 2026-08-01 05:14:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2954d2dd-558b-3d2a-8737-fbe90eb583dd | -4.36842 | -47.76813 | 2026-08-01 05:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 66e6a9f4-3b25-33e5-8f1d-c1dcf57a4f8c | 4.42317 | -60.98248 | 2026-08-01 05:14:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 478d62bf-d004-3be6-b0dd-dd34f9678669 | -3.84798 | -44.0972 | 2026-08-01 05:14:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70a83230-a2ce-327b-93b1-148e8a330ed5 | -4.61456 | -49.0527 | 2026-08-01 05:14:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e3cf0775-ddfa-3d4f-8d96-87cbfc795cc5 | -4.36791 | -47.77152 | 2026-08-01 05:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1467be32-c69f-3344-aa86-b637d23fb565 | 1.09724 | -60.5015 | 2026-08-01 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90701ff3-5640-3f3b-af83-c098dfb2ab6b | -4.37041 | -47.76835 | 2026-08-01 05:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d3a22395-3cb1-3e28-8ed6-13f643c85be8 | -3.11246 | -47.91025 | 2026-08-01 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8a2a3e6c-cce1-3211-b27c-b0f772299e44 | 1.32447 | -60.71481 | 2026-08-01 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8193064-6aee-399e-9963-245db0f85351 | -2.1625 | -47.87274 | 2026-08-01 05:14:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4e3f6c5-cfd2-32df-ac08-ce298aaf0848 | -2.60105 | -47.34196 | 2026-08-01 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41fa7298-16b4-305f-8ed2-dd1dd3268f9f | -3.72826 | -49.27366 | 2026-08-01 05:14:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fdc65bf6-6fd0-3790-8d0e-05d1e882647a | 1.09878 | -60.51151 | 2026-08-01 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6dd81988-7769-375d-b5a6-7c368ae876fa | -2.94925 | -48.95821 | 2026-08-01 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7175b99-7317-3516-90db-1bc1deff0f73 | -4.36993 | -47.77174 | 2026-08-01 05:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a6160770-49f1-38b7-a113-02a3408f44a6 | -3.0368 | -48.41237 | 2026-08-01 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62defa0c-9f6b-3a80-af09-2d78e013935a | -3.8521 | -44.10322 | 2026-08-01 05:14:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ceeaf356-0e32-3906-8021-074044db4e93 | 1.10743 | -60.51529 | 2026-08-01 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 892a229d-64eb-3484-9f73-6662e1a47a20 | -2.88651 | -48.02011 | 2026-08-01 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ea8a2a3e-d7ea-33ea-a692-2e74aefa601a | -2.89266 | -48.01456 | 2026-08-01 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63d21742-0c1b-39e9-bb4e-88602adacfb3 | -4.27144 | -48.19796 | 2026-08-01 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01e76b88-eb12-39e3-b73b-efe8282f8138 | -3.85972 | -44.09848 | 2026-08-01 05:14:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README22.md)
