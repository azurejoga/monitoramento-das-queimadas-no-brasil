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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48b808f7-5051-3035-a66f-429b9171de0f | -9.98452 | -64.79176 | 2024-10-13 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d5bff38-2b31-36fc-afd6-ff4d42fa7551 | -9.9218 | -64.77997 | 2024-10-13 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f85be500-76dc-3378-a9db-7be114dbec23 | -9.91809 | -64.76146 | 2024-10-13 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86314a54-fe4d-3f57-ad59-eb4d537cf823 | -9.91753 | -64.76589 | 2024-10-13 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cd8f068-33df-373d-a27b-9c919460683a | -9.91589 | -64.77905 | 2024-10-13 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0001a181-38ed-3962-9e54-cc98b749a184 | -9.89808 | -64.82505 | 2024-10-13 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c22c459-c721-3f3d-990c-2ab68e4136bc | -9.88788 | -64.8103 | 2024-10-13 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25391009-60e3-311a-ba4e-f8de9e9e454f | -9.88734 | -64.81467 | 2024-10-13 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff4e59c5-4f8d-3397-b4a7-a8129c39606b | -9.8392 | -66.50085 | 2024-10-13 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a67fc602-fcfa-354f-b287-a6ecc0e34023 | -9.83879 | -66.50411 | 2024-10-13 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6441738-e406-37d2-b6b2-68c94e3dba3b | -9.74057 | -64.2303 | 2024-10-13 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e6d57605-d181-3efb-8419-dc10e65fd7ab | -9.73501 | -64.22482 | 2024-10-13 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 19a7a3ea-c0b0-3c34-ac6e-e8824ed2b272 | -9.73222 | -65.06413 | 2024-10-13 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a49730bb-1c6e-30bf-af03-7401e8e4a5e3 | -9.73169 | -65.06837 | 2024-10-13 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f8d295ff-cfe8-330a-894a-93f268c890c7 | -9.72885 | -64.22426 | 2024-10-13 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8d0daa55-837f-3fd1-9553-632323e1b81b | -9.72642 | -65.06327 | 2024-10-13 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 160bb53f-35de-3662-b2fa-39b89db0a1a1 | -9.72589 | -65.06751 | 2024-10-13 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e30fa9a0-a08f-3236-9284-f1e226519063 | -9.63947 | -64.95205 | 2024-10-13 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 292c1ae7-37e3-3ed6-aeb5-a367fafcf5ec | -9.63895 | -64.95626 | 2024-10-13 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fd23d46-1ea8-39ff-8801-b664eb8b6eba | -9.40629 | -64.45725 | 2024-10-13 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 52512a26-b5e5-3776-860b-faabb03762b4 | -9.40574 | -64.46168 | 2024-10-13 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 478a5729-94b8-37b5-9939-ddd9dd7d6840 | -9.40519 | -64.46606 | 2024-10-13 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 13a5145b-77ee-3d98-a36d-87a584f07d18 | -8.67629 | -66.75619 | 2024-10-13 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb90fd24-1cfe-3207-a8b8-65438c4247d4 | -8.67589 | -66.75922 | 2024-10-13 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b2ac2aa-916d-3655-a3b2-bcee4e69b519 | -8.67548 | -66.76227 | 2024-10-13 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fbb3869b-f8ea-3060-9acf-6aa7dd6868a7 | -8.67239 | -66.74629 | 2024-10-13 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38c787d8-3284-34e2-ae37-b49051d760d6 | -8.67199 | -66.74933 | 2024-10-13 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea071783-2868-3fc0-8b68-f922f726427b | -8.67158 | -66.75237 | 2024-10-13 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 009d1108-23b5-3afb-b304-020161c927bb | -8.67118 | -66.7554 | 2024-10-13 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42f62b2b-044e-320f-b98d-5d6e7d52a76a | -8.67078 | -66.75844 | 2024-10-13 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3c0f2b9-d7f2-34d6-a979-3610d59c55cf | -8.66687 | -66.74859 | 2024-10-13 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc3d874f-2a6d-3eaa-a247-89e2b80fae80 | -8.46299 | -66.97675 | 2024-10-13 06:22:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d9887ad-fd41-3c06-af3f-e181c6302758 | -8.45876 | -66.97018 | 2024-10-13 06:22:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d51c8ac1-9339-33b3-b474-079cb9694b0f | -8.45836 | -66.97311 | 2024-10-13 06:22:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0528a221-9cae-3782-9c56-195ffa2f09a9 | -8.19211 | -72.93927 | 2024-10-13 06:22:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d947f6a3-98c8-3efc-ac62-2dddc860854f | -8.11289 | -71.33624 | 2024-10-13 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4ae7371-5776-3961-9a17-35da97617cea | -8.10915 | -71.33568 | 2024-10-13 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4cfd63e4-dfd5-31b8-892b-2f382daf8961 | -8.1085 | -71.34021 | 2024-10-13 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e9aefbe-9ddc-3551-a4a2-5d0321c30701 | -8.03395 | -71.39606 | 2024-10-13 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f28e67b-b9ae-326c-b407-3d6fdd3bf954 | -8.03023 | -71.39548 | 2024-10-13 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f361ca79-8894-331d-839b-653ac5999e42 | -8.0265 | -71.39491 | 2024-10-13 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3cd2e6c2-81d4-3215-b93b-9f87af78f79d | -8.02278 | -71.39435 | 2024-10-13 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b96827aa-c489-3fb9-8ff5-c2ec20af2b43 | -8.02212 | -71.39886 | 2024-10-13 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9615d02-b8d4-3353-a9ab-fbf82fa84b45 | -8.01227 | -71.38813 | 2024-10-13 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfb994a6-e1cf-3326-a9d8-c4af57654525 | -8.0089 | -72.3196 | 2024-10-13 06:22:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b4c8b76-ab50-3f53-86a1-38d43b7f9134 | -8.00855 | -71.38757 | 2024-10-13 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1e94c24c-03cf-3307-bf98-9a0b7790c54a | -8.00535 | -72.31905 | 2024-10-13 06:22:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2d854ab-5d61-3ee4-93da-866998ed932a | -8.00475 | -72.3231 | 2024-10-13 06:22:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd8b124f-da63-3313-aad2-3654cf2e2ee3 | -7.93644 | -72.39197 | 2024-10-13 06:22:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea0ced5e-2afe-3a30-bec3-6e2502c0b9f4 | -7.93619 | -72.39477 | 2024-10-13 06:22:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93924d12-128c-349b-b600-0a6c6f812e47 | -7.85453 | -71.82488 | 2024-10-13 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2136afc9-c752-3f45-be2f-1308b6c68219 | -7.50834 | -72.71036 | 2024-10-13 06:22:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d6385ec-6f6c-3dcb-be08-a1644393c4e7 | -7.42215 | -72.81873 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf977841-d128-3028-b713-a18075eb46a8 | -7.42157 | -72.82253 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad513793-f2c5-3438-a16a-5b5e4f876956 | -7.4187 | -72.81819 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e80bd3b-b353-3003-916f-7d25f018dd9c | -7.41812 | -72.82199 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1682bdb6-719e-36e4-8c07-3bdbd04c9bf4 | -7.37614 | -72.866 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdd4b7e6-7583-3c1a-930e-dad70f1cadfd | -7.35425 | -72.77713 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30563d35-fd26-3971-8dca-068194431d8b | -7.35381 | -72.94366 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e236a66e-0928-31ab-9335-6193bc701c6f | -7.3497 | -72.83092 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f48c1443-36eb-33b1-8149-cd53d9e3a9f0 | -7.34289 | -72.89956 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40915b21-4070-3131-b79d-aa8b31971266 | -7.34232 | -72.90333 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85a42639-5aa6-3ffe-b6d5-d95b11aa8fac | -7.34175 | -72.9071 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f987191-4cc1-36a4-9e52-a30e6ff877c5 | -7.33945 | -72.89904 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01533264-ba0c-3718-9b17-06bc6b59fb62 | -7.33888 | -72.90282 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1fd8051-a920-38ff-8530-b7be8126d252 | -7.33831 | -72.90659 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11f36d9d-ad4f-391f-97ff-e6e23a86064a | -7.33674 | -73.03312 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d158e3e-469f-3c3a-8fa1-e9229fee7623 | -7.32234 | -72.64388 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d042a4d1-ce15-335d-b49e-23adb8d0a8ee | -7.32175 | -72.64773 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d934bcf-60c9-3d65-be79-e3efee8150d4 | -7.26909 | -72.9929 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 689f10e5-5afb-3f07-ac29-096127e6da32 | -7.24357 | -72.54162 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63990aca-dc02-37c6-9518-77d992485a0c | -7.20338 | -72.61855 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87e8633a-13cc-38dd-9910-620ba4a1fd66 | -7.2005 | -72.61414 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b0f764e-0834-3686-aab5-6fa7fee92fb7 | -6.98272 | -71.77409 | 2024-10-13 06:22:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 797d449a-05bf-348f-a8fc-0f83ca246739 | -6.97912 | -71.77354 | 2024-10-13 06:22:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c0ce0241-16c9-3f3e-8c55-2f0294ea5461 | -6.9785 | -71.77771 | 2024-10-13 06:22:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad363d27-cca9-3107-b81a-96c84c1aa73c | -6.97552 | -71.77298 | 2024-10-13 06:22:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87ee82af-ca20-379d-a60b-b108f2f651f7 | -12.48621 | -63.01019 | 2024-10-13 06:22:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2ab1468d-7738-34c7-950e-08de5c5a5444 | -11.72947 | -64.97305 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6d8df15c-ec5f-3169-be9c-682780bd29c2 | -11.7264 | -64.96874 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| efa67510-df7b-3453-9c0a-874330842545 | -11.72589 | -64.97323 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5c6adca4-023a-3028-8ef8-b6f59b19b1ad | -11.72538 | -64.97771 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c2898612-b9e0-3164-b77f-de11cfb67373 | -11.72403 | -64.9676 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d0c2727e-22a1-3024-a8f4-87029d8f1715 | -11.72349 | -64.97211 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 81bba406-5eba-337a-862f-f8b00076f0ef | -11.72294 | -64.97663 | 2024-10-13 06:22:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4237df1d-cd25-3f38-9389-f6984beb5322 | -10.71258 | -68.79137 | 2024-10-13 06:22:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| baedabb4-8c53-3835-af91-a3c702449b3c | -10.64496 | -68.60053 | 2024-10-13 06:22:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77031e96-161d-39be-a5c7-046df0d646f7 | -10.64359 | -68.60168 | 2024-10-13 06:22:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e05e4de8-5dbe-37b2-839b-38b38145cc1b | -10.63953 | -64.43867 | 2024-10-13 06:22:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7dd2337e-c1e9-3f3d-b2fc-c7c5ed9e0778 | -10.63939 | -64.43547 | 2024-10-13 06:22:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07caf0ef-451a-3dd9-b5e4-694a0904f5ca | -10.63869 | -64.44107 | 2024-10-13 06:22:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2de62686-f07b-355b-9aca-46c6b31b0f29 | -10.63207 | -64.44434 | 2024-10-13 06:22:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 606d464a-0560-3aca-9501-53ad96652bfe | -10.42681 | -69.69544 | 2024-10-13 06:22:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62d0bd41-8582-3c16-b1d2-568e97e0019a | -10.40327 | -69.14106 | 2024-10-13 06:22:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8b6027b2-3c9c-39c4-bbe7-9033091f4604 | -11.7308 | -64.9769 | 2024-10-13 06:36:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 25bd6cd3-9655-38a8-9f5f-fb4be1d35f45 | -15.6419 | -59.9767 | 2024-10-13 06:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 05fe31c0-48cc-3802-9448-2d1b0e68729b | -15.6416 | -59.9966 | 2024-10-13 06:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ddc10d06-5768-3eff-a93b-a176eb442fb8 | -7.33753 | -72.90347 | 2024-10-13 06:44:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ee9b14d3-ffba-372a-b559-a766c4f412d1 | -7.33796 | -72.90051 | 2024-10-13 06:44:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4173bd1-ef0b-3522-8d41-17c03032fc1d | -7.3402 | -72.9056 | 2024-10-13 06:44:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README114.md)
