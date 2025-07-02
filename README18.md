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
| b9b9de61-811c-3171-8832-a2f801c7866b | -9.24162 | -50.0442 | 2025-07-02 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3bac08b-5fd8-314d-ad87-a767d43a6905 | -7.88283 | -47.88457 | 2025-07-02 05:16:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 435120a2-8c5b-3655-92cc-de44610811f3 | -11.24071 | -49.49525 | 2025-07-02 05:16:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76e14d05-adad-3fa4-8457-1e26bd09573d | -10.94732 | -54.36945 | 2025-07-02 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6fb881a-06b0-3c78-a9af-3ca48496bca8 | -11.60584 | -65.1468 | 2025-07-02 05:18:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f81c5bf-f529-3469-a2ee-12890e694fc4 | -12.55591 | -61.91077 | 2025-07-02 05:18:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e7f5923-c4a9-36a1-bfc9-2264e5f548ad | -16.0686 | -51.56156 | 2025-07-02 05:18:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a82b710-9cb4-3e1e-8868-e37409c08ebb | -10.88295 | -56.45505 | 2025-07-02 05:18:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7040f9e4-1621-3991-b830-1be5e596e681 | -10.88359 | -56.45062 | 2025-07-02 05:18:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 21907bf4-e37c-338e-a512-875e1e04a269 | -11.74436 | -54.72186 | 2025-07-02 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2319222-4786-3ed2-a051-bbdaf989b98c | -10.88665 | -56.45559 | 2025-07-02 05:18:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 76360fc0-d5f8-3f3d-be3c-fb48633fe407 | -13.38519 | -47.85587 | 2025-07-02 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c46f59f7-6858-34da-b2b3-6651010651f8 | -10.81779 | -56.95402 | 2025-07-02 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52edd517-2bcb-3444-8a5d-45f7adf0c022 | -13.40926 | -47.82066 | 2025-07-02 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6bb864d-f936-3407-8bbd-db5e5f324260 | -10.89338 | -56.46115 | 2025-07-02 05:18:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f22864b9-5001-3de0-997a-0e3250392a16 | -11.748 | -54.72625 | 2025-07-02 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea999ae9-8bd1-325c-8d91-452c608db1bb | -13.38574 | -47.85076 | 2025-07-02 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb58446f-9b2f-3b81-9e31-9ca5c3398f53 | -10.89098 | -56.45171 | 2025-07-02 05:18:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c7a1f46f-f76a-3733-9881-07978ae5059a | -10.88054 | -56.44564 | 2025-07-02 05:18:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6d51b12-74b1-31d8-b3c8-8ce08ccd63a6 | -11.58393 | -54.5666 | 2025-07-02 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d48fc744-56cc-3310-9ac1-43d459d95213 | -11.74611 | -54.72678 | 2025-07-02 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c868d8ce-cfc4-38ce-bb71-e2e54a465f75 | -10.88423 | -56.4462 | 2025-07-02 05:18:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4bd28d16-c942-321d-9b0c-72a4e3639470 | -11.74664 | -54.723 | 2025-07-02 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31799c48-84f7-3123-9b1d-35a78410231b | -11.57556 | -54.56543 | 2025-07-02 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab33731a-3bc3-35f9-a7d1-bc93e2657fae | -15.07863 | -48.9445 | 2025-07-02 05:18:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0262301a-dabe-378a-b7e9-bd26f8382d85 | -10.8799 | -56.45007 | 2025-07-02 05:18:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d17a792-c668-34c6-ad23-55c8b8a1c657 | -9.9559 | -64.9954 | 2025-07-02 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d0ced82-b807-396b-83a9-c487e73a2b78 | -12.4381 | -63.70169 | 2025-07-02 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5eb37344-6a56-30da-a281-91778e80d223 | -11.60981 | -65.14752 | 2025-07-02 05:18:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5a12040-ee17-3303-8abd-ed9fff37cb7d | -11.57975 | -54.56601 | 2025-07-02 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d8730e8-51c2-3c54-a2b9-6e956b3e0f0b | -12.63061 | -54.21774 | 2025-07-02 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42fd193b-7678-389b-99f0-b5781a947beb | -11.74385 | -54.72565 | 2025-07-02 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d429c3f9-1f77-3c6b-ba23-084162a7fcb7 | -10.89162 | -56.44725 | 2025-07-02 05:18:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fe5df190-6b0a-3016-9008-8d6568c21627 | -10.92937 | -57.13102 | 2025-07-02 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1c9b3b66-2762-3878-ba52-e85cee79bfb7 | -10.9258 | -57.13051 | 2025-07-02 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d66e447-7811-3924-b28c-b1e054329b6e | -16.06817 | -51.5654 | 2025-07-02 05:18:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a9be7e3-1ea6-3235-916c-b2007f9a22e7 | -10.88792 | -56.44675 | 2025-07-02 05:18:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4b6c83d2-12cd-3a4d-8faf-569a4d8a2211 | -10.89467 | -56.45226 | 2025-07-02 05:18:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3367f118-6127-35f4-bc37-936d3b501e0e | -10.88729 | -56.45117 | 2025-07-02 05:18:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d91351a6-1cab-3552-abf5-be39f053a8d7 | -12.11045 | -54.5926 | 2025-07-02 05:18:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6e29ae2-1286-3473-98c0-7411da7fa776 | -10.87557 | -56.45393 | 2025-07-02 05:18:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a5df884-74ca-327b-8b3d-d0939abc5e0b | -13.4087 | -47.8258 | 2025-07-02 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7eef766f-5fba-38d5-8597-8165996af990 | -7.6051 | -45.7464 | 2025-07-02 05:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| fb47c2ae-dc15-3a17-852c-f5e5407be8fd | -7.8133 | -44.0358 | 2025-07-02 05:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| c6e9ff8c-d29c-3a90-8962-184ecbd4b003 | -7.8135 | -44.0126 | 2025-07-02 05:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 110.1 |
| b3e2d41c-2afa-34fb-bc66-3afc9d114b5e | -7.7947 | -44.0145 | 2025-07-02 05:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 2e2e988e-dad9-3b9a-abda-baa69d22f739 | -21.04568 | -55.99746 | 2025-07-02 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bd9add9-2ef4-3775-979c-2b521bed4125 | -18.66158 | -55.74859 | 2025-07-02 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2e122197-846a-38c1-8a04-b08ec1134f84 | -20.72656 | -56.65439 | 2025-07-02 05:21:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e8d8e007-aba8-32ad-896a-a972a1564e6d | -19.43572 | -48.55148 | 2025-07-02 05:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e6bddc27-369e-301f-a239-06eedabc4e25 | -21.12395 | -57.53167 | 2025-07-02 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 4d8f23cf-59b2-3e81-9148-74672518aa31 | -18.6573 | -55.748 | 2025-07-02 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d4173583-1593-3c03-8115-1cf98f1e646a | -20.73069 | -56.65513 | 2025-07-02 05:21:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1d562dce-5a56-3922-a3d9-276f8e2b7db4 | -18.66533 | -55.75337 | 2025-07-02 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8e74a439-67bf-36ab-a821-463a7c28ec10 | -19.15973 | -54.83455 | 2025-07-02 05:21:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ace4c3a-5a3c-3c13-8877-0519e6eab674 | -18.42928 | -54.56007 | 2025-07-02 05:21:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5408dec-02b5-3c7a-afaf-62fb81001a72 | -18.66211 | -55.74439 | 2025-07-02 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 4e7a4bab-6015-3ded-b610-929f77177a36 | -19.44124 | -48.55183 | 2025-07-02 05:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bbb07fb6-1788-3a78-b54b-6c09a7a58cdb | -18.42885 | -54.55666 | 2025-07-02 05:21:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c62c76b5-9241-33bd-b26b-0c088c604d17 | -20.54 | -48.75084 | 2025-07-02 05:21:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 914b353f-e246-35d1-be28-f3906b13b889 | -19.43441 | -48.55138 | 2025-07-02 05:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5bcc7403-e0d9-3965-8beb-a210f3f308e3 | -20.73121 | -56.65098 | 2025-07-02 05:21:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e9e972ae-56fc-3005-bbee-840f452bc150 | -18.42827 | -54.56163 | 2025-07-02 05:21:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14954899-e44d-33e2-96cc-e6ebf6f33e17 | -20.72707 | -56.65031 | 2025-07-02 05:21:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b4654b6f-1ba6-327e-9545-56ea71577e57 | -18.66106 | -55.75279 | 2025-07-02 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 32a820ca-96e8-377f-8cd2-ba1b21604cb6 | -18.65783 | -55.74381 | 2025-07-02 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 9f1d2734-a341-36b1-b703-aff7f456172c | -19.22133 | -55.3756 | 2025-07-02 05:21:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 568ef033-d07f-388c-9b3f-a141d20c5990 | -6.2841 | -43.68316 | 2025-07-02 05:25:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| b1d4732a-dbc4-30f6-8b64-41503d11b27b | -5.06563 | -43.73222 | 2025-07-02 05:25:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6062af06-eba8-30c2-b1ae-1f11a2dd9cc8 | -6.27457 | -43.68176 | 2025-07-02 05:25:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 40.3 |
| d38c2914-2bb3-3c89-a420-cdee90a19811 | -6.29525 | -43.67421 | 2025-07-02 05:25:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 2eae11a0-1619-36d4-af48-e2780102b165 | -6.28572 | -43.67278 | 2025-07-02 05:25:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 93e52cd4-cee3-3505-abe7-5691f02c598c | -6.27617 | -43.67155 | 2025-07-02 05:25:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 7162c04a-4151-33f6-b864-341da988ba1c | -6.96111 | -43.0795 | 2025-07-02 05:27:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3aba11d0-dcbb-38f2-9787-906204a5d307 | -7.20222 | -43.07553 | 2025-07-02 05:27:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 6860db6c-d3ac-320c-977c-b9776b2f2828 | -7.79505 | -44.01101 | 2025-07-02 05:27:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 10c157ac-65ca-34a9-9d24-c1ec2e5c738e | -7.79339 | -44.02145 | 2025-07-02 05:27:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 6b8a99cd-bdc1-3eb9-85d5-e6e0d011d6cf | -7.20988 | -43.08646 | 2025-07-02 05:27:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 62b28213-acc6-3380-9d08-23fdbf5cd97d | -7.60616 | -45.73344 | 2025-07-02 05:27:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 2c42b25c-c1e5-3fe3-b8e4-c58226f83c0c | -7.81244 | -44.02437 | 2025-07-02 05:27:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 5f3f4a7d-55e3-301d-b762-4c7a5d86718e | -6.95407 | -42.88337 | 2025-07-02 05:27:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| c2405ff7-e712-3533-a4d8-3b729fca1142 | -6.9526 | -42.89281 | 2025-07-02 05:27:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.8 |
| c4927680-56bf-34ed-95e0-462bd23d8d31 | -7.60404 | -45.747 | 2025-07-02 05:27:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| e780ebbd-c45b-3399-947a-26e4ebbbbcb6 | -7.80457 | -44.01247 | 2025-07-02 05:27:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| dcb23646-b480-3711-8dad-e355a8df4bd0 | -7.78386 | -44.01999 | 2025-07-02 05:27:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 1a5018eb-ac65-31b5-9699-3b696b7c092f | -7.77953 | -44.01359 | 2025-07-02 05:27:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 62dbd3fd-b6de-3977-82cd-679798fc39f4 | -7.78552 | -44.00955 | 2025-07-02 05:27:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2fe3d5eb-3829-33aa-ba45-e50d5fd88a6e | -7.60608 | -45.75421 | 2025-07-02 05:27:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 91e79fcb-41ee-37fe-9cb9-48f8372e089b | -7.80292 | -44.02291 | 2025-07-02 05:27:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 14ccdde6-116c-31ec-b12b-bb96fa350ade | -11.13814 | -43.3265 | 2025-07-02 05:27:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| aefa9f47-b227-3c57-8bd9-527e878fa5e5 | -7.60829 | -45.74065 | 2025-07-02 05:27:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 41619049-7f18-3486-b6d4-b37298dfc194 | -7.81409 | -44.01394 | 2025-07-02 05:27:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| af95b880-352a-3a14-83b5-18f94ebc5023 | -7.21903 | -43.08784 | 2025-07-02 05:27:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 2009022d-376a-37e8-8789-ae6a00877f0c | -19.43322 | -48.55202 | 2025-07-02 05:29:00 | AQUA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 13e225e9-665f-3b46-b038-dfe0ec2e5f0e | -19.43979 | -48.54428 | 2025-07-02 05:29:00 | AQUA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 3cc20159-b8c5-38ab-8efc-df6688016043 | -20.53786 | -48.75011 | 2025-07-02 05:29:00 | AQUA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| ac8f47b1-5b8b-3a34-8b32-9cf119944820 | -15.92422 | -43.51546 | 2025-07-02 05:29:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| cf846742-8ca3-3715-b921-0f819bece606 | -21.85329 | -46.69019 | 2025-07-02 05:29:00 | AQUA_M-M | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 8b5c4681-5673-3402-87ec-2afb8ce47332 | -15.89535 | -43.45754 | 2025-07-02 05:29:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 25f1a42c-9d27-3421-845b-d8a0c063e43e | -7.8133 | -44.0358 | 2025-07-02 05:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |


[Clique aqui para ver as próximas entradas](README19.md)
