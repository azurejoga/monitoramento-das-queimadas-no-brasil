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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46af564b-841d-37d7-80ba-62dbb41f6049 | -15.15727 | -46.41035 | 2025-09-29 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2263f9d9-690a-3d53-ac6c-863e0e0ccd00 | -14.62407 | -48.29062 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c527592-4421-3cb0-9d45-6ab2c7b771be | -14.58781 | -45.02046 | 2025-09-29 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 326583ac-9974-37ba-a662-84a1edfbe239 | -12.77221 | -46.85123 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd2cf166-d8e9-31cf-81a2-58fcac4f11a5 | -13.79082 | -47.88329 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a80803b5-700d-3ff3-8b08-87c2229a3ce9 | -12.7709 | -46.85784 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c900506-91ad-3a47-9eba-81ebfbaacb49 | -13.01571 | -49.45798 | 2025-09-29 03:49:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e616e5ad-8bb0-3abb-b1d0-69ce5cd355c1 | -12.89593 | -47.10586 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1bdc762d-fd77-39e9-9938-8aab7931d915 | -15.04202 | -46.96687 | 2025-09-29 03:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a4e295a9-0871-3699-8514-eee8ef499259 | -15.04181 | -46.96926 | 2025-09-29 03:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63619354-747e-3088-ab58-7b59bd88944a | -23.22786 | -49.40759 | 2025-09-29 03:49:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 891d5b16-dcca-3970-ba86-579665fccb25 | -15.16167 | -46.41046 | 2025-09-29 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3ca709d-5166-337a-a10b-da45ebd02f5c | -13.6401 | -47.33319 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c41a9736-a6d9-3dc2-9baa-73c3eea6b5a7 | -15.02919 | -46.97555 | 2025-09-29 03:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d6c31d5c-0bd5-39be-99ad-c06ea8eecf96 | -12.79709 | -47.7495 | 2025-09-29 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca3a0966-76f7-35e9-82a1-fcb0c852a92c | -13.55746 | -47.27316 | 2025-09-29 03:49:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b5f9e1d-742e-3cb8-aac2-5dfec41a630d | -12.89275 | -47.09219 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ca61ba8-c267-3214-99f2-87e32d2c357d | -19.86454 | -43.53304 | 2025-09-29 03:49:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7fb532c4-c81c-3da8-b16f-447f37a5c500 | -13.82601 | -47.48059 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4db50b4-4bb6-39cc-93c9-087264a67e5a | -12.97021 | -46.24628 | 2025-09-29 03:49:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b2fb7d7-f3ac-3cd6-b9cc-032296c67a71 | -15.03662 | -46.96555 | 2025-09-29 03:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46c5b57e-66e6-3f28-882f-80777581aadf | -13.00961 | -49.43322 | 2025-09-29 03:49:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cbce7a4e-0bf2-3fdf-a846-784da4766b3d | -14.5809 | -48.23062 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e14b256c-ec2a-3267-bff3-c94346410b5f | -14.56388 | -48.25266 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 643aaf6a-6f04-3b75-9d0a-8a53c800d4b9 | -13.82977 | -47.49159 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48b509cc-db6c-3ed4-8de3-bd0197814fff | -13.00303 | -49.43205 | 2025-09-29 03:49:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aad104f0-1228-37a6-aecc-619323724d54 | -23.22955 | -49.40011 | 2025-09-29 03:49:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f358164e-aa64-3b7e-b552-3b10abfad468 | -12.86569 | -46.96345 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f602fd7-20ac-38b5-a17d-f9f52b174b81 | -13.36022 | -47.29882 | 2025-09-29 03:49:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 735cff52-7717-39cb-8c5e-1ac745a84160 | -13.37962 | -48.15688 | 2025-09-29 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| be0975c6-476d-3184-9526-799ff3b15b25 | -13.76886 | -47.91511 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b51635d-cf45-3fc3-80b4-b3ad067dc905 | -12.88398 | -46.98921 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51073fd8-ff92-35d7-ae58-678a514b25da | -13.58251 | -47.29545 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6df0cc3e-a400-3bab-b0d4-e108c136c30e | -14.49506 | -48.54731 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56a505f0-82ff-3313-a91a-e3d20ba07d1a | -14.53298 | -48.42809 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f36384ec-0eb4-3c7b-9114-e25951ee5eb5 | -14.532 | -48.43271 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88a12686-03e5-3ed7-be3f-31a85f870cf6 | -23.74623 | -51.77631 | 2025-09-29 03:49:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| de53201e-0252-3f7b-b588-6e493530620e | -14.68061 | -48.16574 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51e85158-9a9a-3cc0-abed-f91fdddd03e5 | -14.55153 | -48.39949 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2d5b31d-80b3-3df0-acd7-4d188a523ba8 | -23.74505 | -51.78111 | 2025-09-29 03:49:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a07d498b-ee95-31d9-a0b6-1ae51eb947fc | -14.49522 | -48.54625 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14347b72-2182-371a-a9d4-4da150cb64ab | -19.74874 | -45.98769 | 2025-09-29 03:49:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b7a5dd5-3508-3b16-8e6f-dd1d0e055e54 | -14.56875 | -48.25892 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32775e1f-fa5f-38bc-87e2-50c6a647301d | -13.77371 | -47.92154 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f78b20c-7321-3f08-a09f-fc2a9bf78abf | -13.62059 | -47.34171 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29137e68-afef-302a-8991-1959db908b07 | -14.84531 | -48.38175 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b3352bb-f43f-3d30-8fac-9717181c1194 | -15.03477 | -46.97591 | 2025-09-29 03:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d57d9e8-8ba9-3b6a-89e5-48efc494068a | -15.05539 | -42.33737 | 2025-09-29 03:49:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| ff07c0ba-157a-3129-8de9-bf3b6b95ecdc | -14.6785 | -48.16336 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 898f9de1-14ae-3df8-840a-fc4ffd0bf53d | -14.83945 | -48.38007 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29450047-c5a4-335f-9341-dc426a2c333c | -13.23175 | -50.9631 | 2025-09-29 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 07b8068e-c016-3164-9848-b6385b456f7b | -14.42347 | -44.87902 | 2025-09-29 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2de5193-dadf-31ea-bcf9-126bb1d9ecb4 | -13.55658 | -47.26997 | 2025-09-29 03:49:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c027dbbe-1528-38b4-9bfc-16c2bd3958f5 | -14.54499 | -48.4305 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3c722324-5a3d-36c1-9fa4-a12337aec655 | -13.02587 | -49.45352 | 2025-09-29 03:49:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a39a5db5-b12b-3e0c-99fb-54fbb0984852 | -22.0792 | -47.26748 | 2025-09-29 03:49:00 | NPP-375D | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3648f795-4dbd-3f7c-8516-02b426e18a73 | -12.80392 | -47.74626 | 2025-09-29 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a79dc20-5331-3869-a016-7076c54170dd | -23.22607 | -49.41546 | 2025-09-29 03:49:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| fa650b61-ef42-32f6-b7b8-4b393120ceb6 | -14.53693 | -48.43904 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 42864061-c459-3d2e-b9a9-1f9a1b91e613 | -13.79552 | -47.89021 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14d53d6d-1ea3-3824-a3e5-af66aead8bb8 | -23.22412 | -49.39909 | 2025-09-29 03:49:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a36fb847-240b-383f-bbcf-13200b7cd4e3 | -14.56297 | -48.25696 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcc7fec6-a806-312a-bac8-e093425824af | -14.65214 | -48.15488 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e269aff8-5317-380a-9394-38842922a0c8 | -15.26454 | -40.61684 | 2025-09-29 03:49:00 | NPP-375D | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 59324fcb-5147-3bfe-942d-1f587112cb4c | -15.04058 | -46.97408 | 2025-09-29 03:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ae572232-5993-3993-b67a-19cf3981e54c | -13.00089 | -49.4315 | 2025-09-29 03:49:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20294bc9-5e26-3da0-8e43-16d529b27c1e | -13.18104 | -47.44592 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 64ac2401-109f-39f7-984f-8a191f31c45a | -13.78388 | -47.87083 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ac9a1717-1f21-31c0-a949-a0d6a3ca65a1 | -13.81197 | -47.92954 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d87a4ed-e6f5-3c5a-adf6-2fad5587561a | -15.03556 | -46.97211 | 2025-09-29 03:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fac59e22-1cd4-3dc2-8757-bb7a58e261c7 | -14.63114 | -48.28635 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44798b76-23df-3fcf-bc8e-155d1f27c651 | -12.97397 | -46.86105 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d71495e8-0107-3bea-88da-1865552a9a96 | -15.16632 | -46.41443 | 2025-09-29 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11681334-851f-3c8b-be05-a55317562caf | -12.93999 | -46.76908 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f60f5222-0821-3979-967c-0b2cfe78819c | -12.88818 | -46.98991 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1554444-69a6-3915-b32e-32a92c7ab0e8 | -12.8513 | -46.96816 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b06c6c2-3467-3b12-8c10-b441b726d893 | -13.26659 | -48.45517 | 2025-09-29 03:49:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75c26d51-dc97-3571-a078-69fb245b54dc | -13.77924 | -47.86348 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| afc6a1df-1cd6-3d68-969e-3b1fbe9aa6fc | -14.56993 | -48.2827 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89aa384d-7765-39d3-88df-6bc2d63a3533 | -13.58394 | -47.28846 | 2025-09-29 03:49:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b532219-27da-3683-b987-b563e0a88a27 | -13.36014 | -47.29542 | 2025-09-29 03:49:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cea66bfc-3002-37d2-a5e1-71e83ef84a24 | -14.58721 | -44.99779 | 2025-09-29 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe58b9b1-41c3-305e-a629-c52064859bb8 | -23.22515 | -49.41952 | 2025-09-29 03:49:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 0d79e2ad-56be-3b11-8f5a-6e74ca2d7130 | -15.16484 | -46.42173 | 2025-09-29 03:49:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f180f3c-045e-34b7-9eef-7bb339c00417 | -15.26819 | -40.61749 | 2025-09-29 03:49:00 | NPP-375D | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 7b83e9e6-3ddd-36ae-a727-4e0d0d6c03d8 | -12.7639 | -46.86377 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cdaf0bed-b105-305e-98dd-91d048d7e4cc | -13.38057 | -48.15235 | 2025-09-29 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b0bb7eb1-ca9c-3a58-82bf-12898d8798db | -14.75301 | -45.67502 | 2025-09-29 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0703112d-5b7b-3743-b8f1-06eb34da542b | -12.96952 | -46.24983 | 2025-09-29 03:49:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae8a05fb-a9ee-3d62-98f7-93f674cc7ba3 | -19.86687 | -43.83307 | 2025-09-29 03:49:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0d359a4f-021f-3017-b713-3aa8213ac4e3 | -14.54091 | -48.44983 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3ba0e492-2432-3808-990f-a7be602f066d | -12.85768 | -46.96561 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 467c3418-a485-3026-b58d-ed3088c52ca6 | -12.86408 | -46.96291 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c756bbe9-dccd-3de4-b41b-83f6a724e319 | -13.22974 | -50.95636 | 2025-09-29 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8726ec63-9e13-36e1-833e-e0c6d5310abd | -12.93071 | -46.77068 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aee97058-7561-3310-961c-d5f7cfbd06fc | -13.79483 | -47.89356 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e13354fa-cdc3-3895-b01c-052e779d2f29 | -14.51984 | -48.40154 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 608673f5-b4d2-3406-9a8a-4b52acc5a134 | -13.80437 | -47.90681 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 145559f3-355e-3f35-9c8e-c90280d60bf7 | -13.7654 | -47.917 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b2177f6-4091-347d-a842-2a2bbb9b9626 | -14.57876 | -48.2702 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README24.md)
