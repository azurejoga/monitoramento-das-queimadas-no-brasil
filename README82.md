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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74d09724-73e7-3d46-8432-e16afff0fa0e | -11.16281 | -54.016 | 2026-08-21 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 75515b79-9290-3e71-a8c5-2af3f358e52b | -6.85111 | -59.43759 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 42a9acc5-bc70-34da-982b-24595007b998 | -9.41908 | -60.40516 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 0beeef55-4a32-3d37-bd47-ba081b90b077 | -7.34899 | -55.67884 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c7cbec8-75cf-3927-bd17-221d1c9b8a79 | -6.82368 | -59.40555 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b6fb6352-6c1d-3fb2-821b-46e98794550b | -6.36344 | -58.34121 | 2026-08-21 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da9a2489-3ac4-313c-bc41-ca4d75599931 | -8.58429 | -54.75626 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a5bc636-a34a-3f56-b30d-99a0c8dff208 | -6.6967 | -58.94484 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98110c5e-c75a-3461-a466-56afdf0cda36 | -9.40806 | -60.5545 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9885a38f-8c88-3a5e-9e48-1c09deb1225e | -9.20731 | -59.77579 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0460733-ac67-3184-8501-a0c128356153 | -6.10613 | -57.86896 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f4e31d6-35d7-349a-ac45-b3cbcd434802 | -6.58103 | -58.99568 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 20eec4b0-d616-33ef-9821-dc0ced25573e | -9.2167 | -59.7667 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6631a084-0e79-3136-9a17-21f7fe423a84 | -8.38705 | -62.70043 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1b85f37d-1b58-31dd-9f4f-990b74f90122 | -6.84178 | -59.41846 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 158a395f-899d-3a61-baf1-6e4335c54e0d | -11.20703 | -54.00293 | 2026-08-21 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 862ba263-f77e-33d3-b832-668d12d37bb5 | -6.22372 | -55.61721 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| dcfdb3ff-0a9e-3141-9db6-81dbcce6d6d6 | -7.88754 | -61.71318 | 2026-08-21 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2ac16d3-d2d0-3799-8bf3-8800990400a6 | -8.38309 | -62.70357 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2872ab1f-2367-3c9b-a3de-5eb63f40fb1f | -7.87479 | -63.76486 | 2026-08-21 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1d6a67b-3807-3f42-9fa8-c3fb2bacb2d2 | -8.54852 | -55.32322 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96a66a0c-6613-374f-97e1-46e5f75dd45e | -7.88771 | -61.66496 | 2026-08-21 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0b1bc6b-a9ea-3a13-b328-0efc4c8e58d8 | -9.11475 | -61.60623 | 2026-08-21 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7441e6bf-5b27-366d-9d1a-3125a60aca3c | -9.40552 | -60.41763 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 117.7 |
| ab155565-449e-3f8f-b527-0cb73d5df225 | -7.86539 | -63.7598 | 2026-08-21 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc77272f-a76f-36c2-b510-017780b03ed9 | -6.86781 | -59.02652 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d44c8f15-b87b-3537-9924-671235fcc9fc | -6.58068 | -58.97068 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b56f2b6-2814-38dc-b2ca-97cf719ef130 | -6.87826 | -59.4161 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16da640f-331c-3b18-a9ad-5a68bd3f9aae | -9.41555 | -60.42879 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 96d576fe-835b-3aaa-96e9-3fd603374d0d | -7.60681 | -60.95626 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b330a5b-0e26-3315-9279-89b8d0f03c7f | -7.89063 | -61.66941 | 2026-08-21 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64b5c614-3fb5-3399-ad93-42ae7cf73a36 | -6.91535 | -59.35498 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 488732d5-dc94-35fa-b3ed-6a020f7c939f | -8.59118 | -54.74582 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d0be48e-7cef-3382-ab53-f3313d36f134 | -8.0507 | -61.71244 | 2026-08-21 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85c6714e-fa11-3250-bba2-0e07ef74644e | -7.00129 | -59.05014 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f5c6522-c57c-32a4-82ee-a6a4c65f6783 | -6.70928 | -59.09223 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6179d10e-b618-3b9b-a065-00412643bac3 | -9.41301 | -60.41128 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 158ac522-3710-354a-81ae-8c9bdb91b8cd | -6.4275 | -52.76275 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdc7109b-c507-31bb-b87f-95307cbd708f | -6.69373 | -58.93718 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| df4bdd36-6631-37c8-9756-bade2a28c854 | -8.18216 | -54.98975 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15d147fd-23e0-3eca-a45b-2875e4c8ce76 | -8.28802 | -62.89388 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73843888-4a3f-3d2f-99fe-79dd2bee2b8b | -6.85574 | -59.0248 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a369da4-6e40-34d8-9086-ea0e5e44cd7a | -6.11465 | -57.69346 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac8b6d4b-fdd3-3531-a6bb-013cde19a84b | -6.82442 | -59.40059 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ee10d375-ad04-3414-9b13-5a82b0eb69df | -8.66807 | -54.59089 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b1c6b09-bd75-3c73-898c-ba7fa293942f | -6.86358 | -59.4344 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2bb8e794-78c5-367b-bdcc-9538229eb88f | -9.39525 | -60.56452 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7db22ca-84fb-3389-be66-14d8406ac802 | -8.57526 | -54.78021 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f30c3a68-33c3-3787-806a-4916855b758d | -6.10182 | -57.86838 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50b0003e-588b-387d-a16c-59c33d15cd8c | -9.40042 | -60.55581 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f09690f8-9e9e-3dc0-82df-376632d7ea3b | -6.66673 | -52.88976 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 343d1d74-e6e7-3538-bab6-f9f748ba0c28 | -6.8768 | -59.42612 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 87d8c302-76f2-38ee-aa5e-c844606dd25d | -6.79332 | -59.58202 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e4c9050-1b52-3839-8667-832eaf732712 | -9.4017 | -60.41704 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| a3fc6d93-b34c-398e-af52-0d5fb58695cb | -6.01739 | -57.82784 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ffee2d4-6318-32a0-a3e6-9d37bc664a64 | -9.40049 | -60.55337 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acdb9a55-ce7c-3881-a275-ea4be646f1cb | -8.57408 | -54.66427 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10c41c13-349a-325a-9329-5c1684fced56 | -6.89028 | -59.44344 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 01646815-046d-3ae0-a9df-92c1088435c0 | -6.87753 | -59.4211 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4bc33264-2ac7-3967-8f24-02dd988cce98 | -6.8704 | -59.41498 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a517338-e41f-31e9-93d6-c292a6c2e7d7 | -11.1688 | -54.01677 | 2026-08-21 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cb86570e-504f-3e2e-905c-7a429d5e6d82 | -9.21614 | -59.65639 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06cc7ba1-ddab-3a1d-8cb7-e4ac1eb4e4a6 | -6.92397 | -59.35112 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c76c185c-9d0d-3be3-bb4b-115f35e4c339 | -10.82008 | -50.99999 | 2026-08-21 05:42:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 425252a5-c6b8-3e42-b4ba-15846b04f2d2 | -11.20728 | -55.06844 | 2026-08-21 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27ce2610-ac64-3401-b5fb-faea52b59305 | -6.55508 | -56.2604 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 615b88e3-7415-3f4a-a8ee-6ef091e6eb7f | -6.89493 | -59.439 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d7a45889-8828-3cce-ab06-5a6a68a43cfe | -9.20878 | -59.76552 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 541d01be-7c74-3781-b78a-73d5f9b14e2a | -8.66857 | -54.58706 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4336903e-3c96-37da-9b20-e50c2d61073e | -6.89101 | -59.43844 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3090e63d-f92a-331c-94f9-ea0f9e770af0 | -10.24748 | -54.36335 | 2026-08-21 05:42:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8c1f23e4-56a3-384c-8ce2-e485f4ddf539 | -9.11536 | -61.60217 | 2026-08-21 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1d6242a-593d-31a2-80df-a6e7e39057a2 | -9.41526 | -60.40458 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 41ade72f-9333-3d30-9abd-f438879e409f | -6.65495 | -56.34222 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec2bafca-4294-3810-8b4c-5a7286a47d3c | -9.41315 | -60.41879 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| e9f06353-f9e5-34e0-8fcd-857501157f53 | -8.5837 | -54.75944 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aaadbc0a-cc2c-3fd1-9691-d99c0d9611da | -6.22907 | -55.61992 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 5a80d8e0-5d11-32b0-9736-ab41fdad2ba1 | -6.57457 | -58.98406 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f34e1c6-96c1-3a1f-a8f2-912cb9ce888a | -9.41929 | -60.42194 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bd14aad-3198-31fa-86ca-892fc0f31404 | -9.39291 | -60.55228 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6a710e8-f67b-370e-87c5-9c426d40bebc | -6.87142 | -59.43554 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| beaf62c5-87a7-337a-babf-3bb476a9f505 | -6.84103 | -59.42345 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce537cf0-6f84-3a18-9446-bd1b87148906 | -6.01138 | -57.8262 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 61050c66-df3a-3c59-ae49-8549259a39e4 | -6.72477 | -59.09803 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f80655d-02f1-34a3-9082-2ffe975ae074 | -6.38586 | -54.94721 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9029359-efb2-33d1-9c20-5c1c665aef1d | -11.20388 | -55.06517 | 2026-08-21 05:42:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97200267-c6af-3a2f-971e-296b0b866ed0 | -7.5483 | -55.56044 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c57a0896-33fe-3815-82a6-e5def1f215ae | -9.41413 | -60.43079 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ff5ae79c-57e3-37de-b594-c9bf204a4981 | -9.40412 | -60.42704 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 59a8b9dd-a2ab-3570-aa9f-4b86253a1f2e | -9.22013 | -59.65696 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01f7b623-1cae-3afb-a3c0-bd381bbcfaa0 | -9.41696 | -60.41937 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 9e6d72bd-b00f-39e7-8201-9efbd51b654d | -9.20178 | -60.7756 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ae12988-a279-36d4-87ed-ce900d3efe27 | -8.39101 | -62.6973 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 50d37442-0d9a-3467-b60e-82fe11d1976d | -8.55381 | -55.32407 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5633c0bb-f3cc-3995-b164-69f0a9898121 | -9.22242 | -59.78328 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f4cd209-b117-3c00-8f7b-9f20c6e5e4d7 | -8.18258 | -54.98668 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cec0571-5695-3a9f-9ea1-fadbeae36a1c | -9.44993 | -51.60875 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 773ecb88-365f-34db-abc6-d98e74cebb3b | -7.5992 | -60.95226 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27d8651b-fa56-323b-9eea-39c909fea5c6 | -8.52024 | -55.33281 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b4f2bfc1-f482-38a1-9539-458b6fedf58c | -6.6897 | -58.93652 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |


[Clique aqui para ver as próximas entradas](README83.md)
