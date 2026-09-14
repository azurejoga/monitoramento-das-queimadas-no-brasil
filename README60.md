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
| 824e2a98-be61-3bf4-84d7-f731bc0f9cc1 | -8.71416 | -62.56055 | 2026-09-14 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 21386361-f20e-3c26-958c-8015e5ab8619 | -10.66946 | -54.15335 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 338614a8-62c5-3462-b777-9eb8dd2d120d | -10.67698 | -54.14114 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bac67987-d1c6-33ec-9c2e-6b33927b7642 | -10.68447 | -54.12912 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 687192a6-0fad-32a6-892b-7326f24014df | -10.69462 | -54.13153 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82c90418-57ce-36de-a32d-4cb1ee95719e | -10.67591 | -54.13798 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8f2128fa-fd1b-33a5-833d-55a609501ee8 | -10.69022 | -54.11829 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cfa66eb9-c8fa-3bc1-9f51-3dba0a659bb8 | -10.65772 | -54.14016 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6babc5b4-8cc3-3e46-8851-91ee2d180dce | -16.23222 | -52.64787 | 2026-09-14 05:38:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 23bca0ed-35d3-3ecf-b0f2-11dd77db210a | -9.59437 | -55.14848 | 2026-09-14 05:38:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f247e0e1-8bbf-3ef5-ad45-3fb931822715 | -10.66356 | -54.15277 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 56b59ea3-e7d1-347e-8b7d-595fed061858 | -10.6834 | -54.13766 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| de24018e-a906-3200-86de-9d525bc2c484 | -8.54765 | -54.71358 | 2026-09-14 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b253e7f-2ac9-3d19-a3a3-1dac2804c38a | -8.53665 | -54.71194 | 2026-09-14 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ee5f80f-5e74-3244-a064-792df0ad5dd9 | -10.68667 | -54.1481 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0236b2a7-8243-39bd-8823-726d6e7c6f39 | -10.68078 | -54.14729 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 0091d0e0-3889-3123-9340-25d47b74f4a4 | -10.67285 | -54.1638 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 37.3 |
| a723d3a1-23fa-34ec-bbc3-db25fe8b7abd | -10.66786 | -54.16618 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7f27ac78-a446-3f28-9f8e-ef1e3d3d5386 | -9.26778 | -59.63759 | 2026-09-14 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5208ad70-9b49-317a-8b75-db67de977acc | -11.26167 | -54.13434 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| adb30409-6259-3446-b187-6db5bd3cd5bd | -10.68381 | -54.12185 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a745cc3d-ee14-3f60-bf6a-c0d94a5e8b3a | -10.68431 | -54.11756 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16e2a7db-aafc-3ca6-87b9-af014b891a11 | -10.67101 | -54.12883 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 359ee65f-71b1-332f-bbc2-480f6d1c72f3 | -10.66518 | -54.13978 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 67e40ee7-7217-33b4-8cd0-2860a7accdea | -9.59396 | -55.15175 | 2026-09-14 05:38:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b3611ac-85c2-322d-925b-bad57cf56c0c | -10.68715 | -54.10784 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e35eff56-1ada-3680-906c-400990c4cbdb | -10.67427 | -54.16264 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 369f097b-0706-3119-9f6f-0c405cc6c5f3 | -10.68561 | -54.15699 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e9630fc1-fc75-37b8-9257-c56880b68b9a | -9.58215 | -55.14218 | 2026-09-14 05:38:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0defce28-a50a-36a6-81e7-dbff1b9c8b27 | -10.6567 | -54.14885 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 079edf65-bfd2-3588-b2fb-f61597b6d7e4 | -10.69097 | -54.16211 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9bbf0b5d-1ecc-3d0d-add2-168f412efd65 | -10.67151 | -54.12455 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b2b2284-6d83-3be7-91a3-32a5e71335d9 | -10.68499 | -54.12499 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b27d2308-cff8-3c0a-89a8-f1200b9c2322 | -8.54214 | -54.7128 | 2026-09-14 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 367af70d-c092-3d26-8cc1-e49fe794d94e | -9.6885 | -54.84616 | 2026-09-14 05:38:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e839d30-e39f-3731-acd2-d20aa8af3734 | -8.76841 | -61.39864 | 2026-09-14 05:38:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad889ece-d675-3b0a-9786-eb773da4aac0 | -10.67535 | -54.15407 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 667cedb3-e06b-3bc3-869d-3136a1e8e974 | -10.66157 | -54.1582 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 7636bd19-9e11-3347-87a3-caf3555098ae | -8.8215 | -61.41082 | 2026-09-14 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| caed3956-a154-39be-a2fb-6d5208379570 | -10.46536 | -51.24647 | 2026-09-14 05:38:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6098051e-e327-33f9-8730-106861d148db | -10.65821 | -54.14771 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| cf04be5d-18ea-3fe1-b3dc-e240320a7027 | -10.67907 | -54.17198 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5cf61b7c-8388-3f98-90fb-72d22e9b1f3e | -10.6818 | -54.13874 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5e5aba54-d402-3134-af91-8b8e73b2875f | -10.67742 | -54.12518 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bf88ac4-196c-3851-9079-cda6eaabda06 | -9.68341 | -54.84183 | 2026-09-14 05:38:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 355e4c1f-cfa9-392a-adde-1afa6d3a7f70 | -9.20882 | -59.37976 | 2026-09-14 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f4ee690-f185-3b64-a26a-8634bfba124a | -8.81792 | -61.41026 | 2026-09-14 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2f9720a-200e-3000-b05c-34d567341b13 | -10.67911 | -54.12415 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4a79b49-a9e1-34c0-a50a-e594a9b2afbf | -10.65132 | -54.14376 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6fc5c878-980c-3e2b-8e90-df3acc02bf09 | -10.67161 | -54.13621 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 91bd2a31-1ba5-3793-a5ab-32851efec58a | -10.67964 | -54.11995 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e828786b-3411-36e7-8094-e10d74f34584 | -9.13998 | -51.58509 | 2026-09-14 05:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8fa05a69-251d-3d7e-9e8b-3925dd6f0cc2 | -10.6732 | -54.17113 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 10e6068f-c7da-37f7-a045-1d884286b175 | -8.93742 | -61.45105 | 2026-09-14 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b56bae87-be57-3b82-9e6f-4d9c01f17be0 | -10.6754 | -54.14226 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| f5316f9a-bb55-3943-a7e6-9c79e00db06a | -10.67001 | -54.1373 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 2e3cc0eb-3e6c-3e7b-be12-568ecbdd24e6 | -10.66747 | -54.15882 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 5e6688a9-6378-3135-b51a-ad5e181529cc | -10.65286 | -54.14269 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b05870e2-286d-3ba4-93dc-65f6570e59de | -8.5436 | -54.70181 | 2026-09-14 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4725da7-febe-3c18-96f2-71b952a6c15d | -10.67822 | -54.16889 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0befafa2-48ad-3cb9-92ce-4e0315263e63 | -10.68358 | -54.17401 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a28a3bda-790b-31c4-ba49-8c16428b5a60 | -10.25626 | -57.69333 | 2026-09-14 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cae0958b-75c5-3fb7-8b53-e0b40e089920 | -10.54929 | -51.30869 | 2026-09-14 05:38:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 18ddd95a-f336-3fc2-a857-96ebe3a4e82c | -8.53858 | -54.69727 | 2026-09-14 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e06c0e58-001f-3528-b587-11185f07d7be | -10.669 | -54.14586 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 170.9 |
| 7bb219b9-d2b2-33e1-85b0-c95ec5cbd9bb | -10.67873 | -54.16464 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 61669055-92de-3276-9783-be3768fb1a65 | -10.67644 | -54.14541 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 51f28473-1b16-3b31-972a-7a6ce83af0bd | -10.66646 | -54.16738 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1e526f91-76ff-339d-a02d-09261314c104 | -10.68018 | -54.11563 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9047a2ee-d4f8-3cd1-b052-73486cfd50e9 | -10.68231 | -54.13445 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6b88d027-4533-39d3-9543-ee7879727f0f | -8.54167 | -54.71642 | 2026-09-14 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74a200ce-d85f-33d4-9884-38c4b74f0746 | -11.26219 | -54.13007 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 22265d30-87da-3a75-ba17-c8126b76eeca | -10.68971 | -54.12257 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9263f8e-b2e8-343d-8ec5-d6adf69c23dc | -9.98821 | -59.86558 | 2026-09-14 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 529a7f0f-e7f7-3a96-b47e-c2224597f44b | -10.68996 | -54.17059 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1689f1e5-2894-3d0c-b6fd-ac5879780238 | -9.00046 | -50.82041 | 2026-09-14 05:38:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| e70c7f7e-bb28-35b0-9b57-93efc843e637 | -9.14066 | -51.57953 | 2026-09-14 05:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8de5ba16-a719-38c5-80c3-553f4d155c7b | -10.67336 | -54.15953 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 39d17890-c8e9-38e8-8348-9ba9452f50b3 | -10.67267 | -54.12774 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 230e6f0b-197f-32bf-be81-53c2c762a0ea | -10.55015 | -51.30126 | 2026-09-14 05:38:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9f28318f-b187-35d2-8954-9a9b26abff4c | -9.68294 | -54.84554 | 2026-09-14 05:38:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16f5f7c1-da1b-39c3-b546-e17fecaedb69 | -8.54263 | -54.70916 | 2026-09-14 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a4228a8-cb32-3fe4-98be-3e0ec4f48534 | -9.72158 | -54.35716 | 2026-09-14 05:38:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c30ffe7-6761-3080-a9c3-755b3753d94c | -10.66302 | -54.15706 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| dfb1d57d-3037-32e7-aa6a-2f6254c78165 | -8.53568 | -54.71928 | 2026-09-14 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bce9d5c2-7c54-3c0d-8346-f8173af8f7a2 | -8.82088 | -61.41494 | 2026-09-14 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 209b9d1b-ff0b-3ee2-b5be-a8c1c9d5b214 | -9.70812 | -54.37174 | 2026-09-14 05:38:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9adf5c5a-56af-3e84-98d7-3f63c689c1fe | -8.5441 | -54.69806 | 2026-09-14 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9169ab82-8d68-33db-89c2-6971cb62ff71 | -10.65183 | -54.1394 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e8c054dd-f6ef-3372-a7e2-e628f841d578 | -10.67792 | -54.12097 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b1ad887-ff9b-310d-a950-401416dd156b | -10.68181 | -54.10266 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d78e549-77f3-31e5-948b-1c97906d5da6 | -10.67975 | -54.15604 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 249.6 |
| 6412ad1b-769d-3781-96bc-30b0f82b3e70 | -10.67438 | -54.15089 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 249.6 |
| 7447f964-f4eb-3e9d-a12a-f584c886391e | -10.6534 | -54.13837 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d4b30d6d-ad49-3097-98cd-6de2a675cf07 | -11.25677 | -54.12497 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e29d3231-db18-3d91-8098-4b5f8c3f131c | -8.77557 | -61.39971 | 2026-09-14 05:38:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c10e9434-02a9-3266-9c9d-fda865e06404 | -10.68613 | -54.15261 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 87502314-e30c-3f61-9620-a25af3f9c84a | -10.68552 | -54.12085 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8720a621-ae55-34b2-a98b-942126db5dd4 | -10.66311 | -54.14515 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 170.9 |
| 304a0d94-374d-34ee-91c2-f7b8876ccf20 | -9.07162 | -61.01405 | 2026-09-14 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README61.md)
