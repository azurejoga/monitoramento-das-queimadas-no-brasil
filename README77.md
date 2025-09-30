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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 221337c1-f599-3f48-bdc6-5c9ae2306f80 | -16.06881 | -51.03769 | 2025-09-30 04:42:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac9f5a63-2167-3a44-af1d-6cfdfaa73c5b | -14.51533 | -48.45241 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| bf1a69bc-e020-304e-b8b6-fae8bda29fa2 | -14.54716 | -48.48152 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 594115ef-89b0-3a41-a8eb-0369ffb8463d | -16.089 | -48.10924 | 2025-09-30 04:42:00 | NOAA-21 | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0527a272-67d4-3fc1-a5f7-cf0fd0fbd043 | -15.24686 | -48.74443 | 2025-09-30 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1c2a2283-77e8-3404-acf8-6da6b0c798fa | -18.021 | -46.69949 | 2025-09-30 04:42:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f89403b-4202-37b7-b234-686d97353f21 | -14.71209 | -48.15644 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 397f6228-4dd6-3b76-833b-2e2e4b2c209e | -14.47281 | -48.5715 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ff2cf7c-e4e3-3c97-acbe-e0eba9052f35 | -15.25531 | -49.71279 | 2025-09-30 04:42:00 | NOAA-21 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68f1a221-d671-36d6-be8d-702252258519 | -16.42484 | -47.03854 | 2025-09-30 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 41307c90-3894-33bd-9236-0bab6c879638 | -15.27812 | -49.50914 | 2025-09-30 04:42:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b0c3c3ff-20b6-3629-b5d9-e21548c88874 | -15.92802 | -46.21419 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| bf2a434f-26c7-3d7d-bc84-948ce20649b3 | -15.84275 | -54.97661 | 2025-09-30 04:42:00 | NOAA-21 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86c05ea7-f446-37fd-9dcf-2365a6a1b02c | -20.39175 | -43.68105 | 2025-09-30 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4aefd9fe-ecd4-38e5-aa25-48bb17980961 | -17.91548 | -57.58665 | 2025-09-30 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2d7dc564-7c5f-3c1f-aff2-bbc0a82a547b | -15.47466 | -47.9376 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3ab95443-d807-30ae-af23-29775e5beb1e | -14.79627 | -48.30345 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 40f1c524-ca01-3ea8-877c-a6427dc79cf6 | -14.5266 | -48.44979 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 390b9025-d9b8-36c2-855b-72575956d031 | -19.60248 | -45.89236 | 2025-09-30 04:42:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c90ce3b3-4e5a-32c9-99b8-daa1d64aae81 | -14.9608 | -49.54696 | 2025-09-30 04:42:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68be7091-837d-3b3b-9e95-ea4a95867bb1 | -14.5425 | -48.23861 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 986a7f21-269c-34dc-8c37-5e58a96a8ed6 | -15.38556 | -47.06844 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a2c316a-16cd-3aec-9116-24e3d37ff8b5 | -14.7066 | -48.14308 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| a68cdda8-3bc7-3b7c-b906-df116d60a7b5 | -15.4193 | -48.22235 | 2025-09-30 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f730631c-1741-3a3a-b5a5-92fc5307afff | -15.55109 | -44.35595 | 2025-09-30 04:42:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 14.9 |
| c515c5ad-10ad-3c18-98ea-3132f1b4c8e6 | -16.61332 | -49.20108 | 2025-09-30 04:42:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 957d524d-29d6-364d-a7b3-3188e5178293 | -15.20116 | -49.55557 | 2025-09-30 04:42:00 | NOAA-21 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b07e5b57-16fd-3f20-bcf4-102871ed9028 | -20.09886 | -45.32008 | 2025-09-30 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ef2135f8-6d1a-353d-8fbf-640b7b094036 | -14.5172 | -48.38913 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ae45eaee-f83a-3e7e-bd72-f9326fa97a6c | -14.51592 | -48.4483 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1cf5adcd-3c2e-312e-a391-8d36e696c5b8 | -20.74399 | -47.14589 | 2025-09-30 04:42:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6056f726-f137-3d23-b1d9-6a5fe2a44b1e | -17.91942 | -57.58792 | 2025-09-30 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ef6b190c-2c6a-320c-8eeb-d083de1634b8 | -15.27292 | -49.25913 | 2025-09-30 04:42:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a3a6963a-63f4-3ffd-9c7d-2180e63e8761 | -17.72175 | -46.6699 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5369ea2-9e16-3e88-80b3-8b519f189199 | -15.85873 | -46.23249 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62249eec-11ed-337e-b458-94f465725bc6 | -16.53243 | -49.43188 | 2025-09-30 04:42:00 | NOAA-21 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e14c943b-98e7-326e-b5bb-09c60e980e18 | -14.6907 | -48.14154 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 15daddc4-dd73-3b8a-b63b-6d33fd2f922b | -15.49506 | -45.8742 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a111ca5e-9918-3816-be06-72108dfc5777 | -14.61725 | -48.29515 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d93f47b-65b6-31c8-9bd3-2ef712d83b98 | -18.12327 | -42.19495 | 2025-09-30 04:42:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| ef0b2dab-41e0-3486-8a39-528fc8b14324 | -13.73459 | -54.72213 | 2025-09-30 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bb42c76a-8d96-38bf-a278-dbca487809eb | -17.70986 | -46.6697 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44535543-2b55-3f12-b130-1582bbf9450e | -15.27354 | -49.49242 | 2025-09-30 04:42:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4b41a13-f05f-3612-8fa9-77c693daa0f7 | -15.72143 | -59.51587 | 2025-09-30 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 405239e9-6361-3d7d-bc3f-163c5bc4d05d | -14.52968 | -48.37831 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d8d9105f-9fbb-3a4a-bb78-6557eabfb9e2 | -15.90703 | -46.24628 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 191593ad-8a68-3f27-9932-b82676ebd8ff | -14.546 | -48.48969 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 35fd4a38-8e43-3c55-9a64-864dd2449fb2 | -15.55571 | -44.35658 | 2025-09-30 04:42:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 3a816815-b2dd-3e7e-9e60-7670fa7144ad | -17.34736 | -53.22372 | 2025-09-30 04:42:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e6d9b3d-a400-3afd-a4ae-9d5359a9c976 | -17.23582 | -44.11092 | 2025-09-30 04:42:00 | NOAA-21 | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 392e842b-94c8-3764-93f2-da5c8e6191fb | -14.68704 | -48.16686 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 573703a6-58b2-3fd4-b0ee-fc7e1344d368 | -15.91524 | -46.24741 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c1375ad3-ed6f-3df0-81dd-0f77ce7f6f7d | -17.71959 | -46.65387 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 15a35c7d-12d9-3225-b2da-9f7004ad4538 | -20.41572 | -43.34956 | 2025-09-30 04:42:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 44864678-5bba-3374-8cb9-10d7cfe6720d | -14.71437 | -48.24513 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29f6813f-1aa3-3856-b2ab-83a89b64931c | -16.74725 | -44.92409 | 2025-09-30 04:42:00 | NOAA-21 | IBIAÍ | MINAS GERAIS | Brasil | 3129608 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fee5bb4-885e-3e12-9dd7-bfc742cbb6f7 | -15.2508 | -49.7198 | 2025-09-30 04:42:00 | NOAA-21 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3606e59f-d61e-3b12-be4d-d12592aeee40 | -15.24401 | -49.71871 | 2025-09-30 04:42:00 | NOAA-21 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b984ce9a-5c30-3242-8bca-eed539039b49 | -20.09367 | -43.8996 | 2025-09-30 04:42:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 430c1685-d1eb-3302-9677-a5bb8daf9d89 | -15.29038 | -56.79139 | 2025-09-30 04:42:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a040a1e-dbe9-31d1-8c3a-71e8dad09246 | -14.48869 | -48.56147 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0801cc03-140d-3e1b-a43d-50eab8fc9787 | -14.51536 | -48.42712 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2ce5c17-dc0a-3248-8f3e-7645e7bad4a4 | -15.17578 | -46.41389 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2feff41d-0b9d-3c9a-92a4-0cc37e5de7c4 | -13.75575 | -54.73027 | 2025-09-30 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd5b28cb-4498-34bf-a505-54e6e861388f | -14.54296 | -48.48676 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9287dd34-0bb4-328a-89b4-48366e3e7588 | -15.33177 | -46.2674 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4b799c4-43bf-322c-9966-434a05eb0319 | -15.47403 | -47.94203 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c79ed81-de48-356e-8c8f-cfb29774acf4 | -15.50027 | -45.86684 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ae3d82a-7b0e-35a1-81fc-7b5d41e3003a | -15.36519 | -48.62567 | 2025-09-30 04:42:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b81007be-611d-3b6c-9da8-94890ed89792 | -17.88736 | -57.62541 | 2025-09-30 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| b5f70944-2d02-3780-90c7-b001806fd963 | -18.53355 | -46.04607 | 2025-09-30 04:42:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 5aa5e56b-a080-3ade-ab11-1feb3b31f2b1 | -17.71643 | -46.64574 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8ddf49d1-cb4e-3db8-b131-56591bc71412 | -14.6929 | -48.24112 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 11669a73-648a-309a-bf41-d42b67d61488 | -15.39325 | -47.06991 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 29b20135-1d95-38c4-9391-db1d5d37c8b6 | -17.9204 | -57.60535 | 2025-09-30 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1a95eabc-ef79-3dd8-841f-9c8365393aef | -15.66002 | -51.33058 | 2025-09-30 04:42:00 | NOAA-21 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb53a866-9043-3b7b-a212-9a1a9736d7a9 | -17.71232 | -46.6453 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2425470-4183-37a4-bf4b-db34e2f39898 | -15.29106 | -56.78765 | 2025-09-30 04:42:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb9c9c66-1437-3485-852e-944b376631a7 | -15.7177 | -59.50955 | 2025-09-30 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8fbf8480-28b7-3e01-acda-373d133b12be | -15.48252 | -45.87258 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66a5f880-5e4a-375c-86a5-8c13a3b3cba5 | -17.71765 | -46.6694 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86b85a89-d921-3e28-94af-a3182b828e4a | -15.4692 | -47.92306 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 06d3a38a-ea06-3575-b137-c66c8e42fc65 | -17.71339 | -46.64283 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d85ca600-b85b-374d-905f-158dd9fe4f4d | -15.4865 | -48.56213 | 2025-09-30 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30d843c9-3ebf-3a83-b8c0-c9d0eb64c3de | -15.71391 | -59.5036 | 2025-09-30 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8e31a96-5f18-3151-b91f-d5f327061a55 | -17.40626 | -47.14774 | 2025-09-30 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ef416158-8a85-3ba7-9c33-b6d30a3a7487 | -15.85717 | -46.24461 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| adf7b156-6b15-32f4-8a12-1f70a5bb454e | -15.17207 | -52.81992 | 2025-09-30 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 859ae641-bdf8-34df-98d8-b8a37872e100 | -14.54661 | -48.26097 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d9dc1ee2-949a-300a-8aa3-bfda789a5a45 | -14.73391 | -45.66524 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 02b891ea-a451-357c-88c6-a8d9719f96c4 | -18.53564 | -46.04452 | 2025-09-30 04:42:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 00fa5c21-8571-36df-9e15-e7a0772c6b70 | -15.68093 | -46.26178 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a3e1b06-c56b-332c-934f-7abdbb2db946 | -16.41242 | -47.04163 | 2025-09-30 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c93fef92-c435-3e38-b4b9-fb396494d5ba | -15.2474 | -49.71928 | 2025-09-30 04:42:00 | NOAA-21 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c6558be4-7bbc-3524-b7dc-69a47b54f76a | -14.58678 | -48.27776 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8859c919-4851-3b59-b130-dd3cee57923a | -15.88179 | -46.21576 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d29212e-dcb8-3036-9e1b-6af4b909429c | -15.25872 | -49.71321 | 2025-09-30 04:42:00 | NOAA-21 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| deee7a59-64b0-3737-ac82-0df4e904eb82 | -15.375 | -47.07527 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ae04492-3340-3c66-b2d6-f599eb7d8906 | -14.54245 | -48.48919 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b4a749c5-6c3f-383f-bf93-2a758fc88d82 | -14.69891 | -48.25058 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README78.md)
