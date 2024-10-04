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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16d57206-77f4-382d-8af1-d44248409fb2 | -12.79177 | -47.44308 | 2024-10-04 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bf10535f-4ab9-30ec-a141-c6608b648a8f | -12.79121 | -47.44684 | 2024-10-04 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| cb5203c2-288e-3b7e-a44c-34c89a38ed62 | -12.37962 | -47.68112 | 2024-10-04 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab512c4a-468c-3f18-8dd8-6c200232c017 | -12.37906 | -47.68481 | 2024-10-04 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8501b193-8e34-30e2-92ea-0a9237d51371 | -12.29058 | -47.64902 | 2024-10-04 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84b8566c-3f94-3dc3-8e50-d6829e07bc53 | -14.27643 | -48.15847 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f97b5aa5-4e5a-374d-b941-c29bc10efb61 | -14.06857 | -47.89747 | 2024-10-04 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc4b7357-945e-35d0-b0a6-7b55b425d75a | -14.06801 | -47.90122 | 2024-10-04 04:34:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9334ef0c-461e-3e5d-aebc-b94ebee3d0c5 | -13.7342 | -48.14971 | 2024-10-04 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b498601d-b61f-32f9-bd68-9903be307f89 | -13.73364 | -48.1534 | 2024-10-04 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40c36eab-8265-364f-a061-22f3a3d8ecc9 | -13.73084 | -48.14912 | 2024-10-04 04:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad5df4e0-dd31-381c-a905-c0aaec3bfd9d | -15.25303 | -47.13878 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7b3c294-277f-3b5b-9d8b-a4e654c5dfaa | -15.24597 | -47.13766 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3ee1bee-5381-38ff-a604-fe7f97360ec0 | -15.24244 | -47.13704 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34caa0c7-28a0-3eef-b097-99fa07c48355 | -15.23478 | -47.14005 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a5f385f-8990-39f7-8e0a-b7926fc86f8f | -15.23126 | -47.13939 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca733e34-aa39-33e5-91b5-de2202e23171 | -15.23005 | -47.14782 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 800093a9-0d19-3466-877e-51f2b2ba403b | -15.22653 | -47.14713 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f8d05aa-c190-321b-9737-7ab46180c921 | -15.22595 | -47.15118 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7088e2fc-2cc1-3936-b45d-ffc622ee20bc | -15.22243 | -47.15052 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d61c75f8-b352-34da-b027-7f2beaeabe33 | -15.21364 | -47.50611 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f2d37c4-1a1f-3921-b473-5d103e01840c | -15.21299 | -47.51048 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6c73f6b1-5c26-3a8b-bfc9-42e9b5ace8b1 | -15.21017 | -47.50546 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cc0a3bf-3655-31ba-bfc2-6a7a00900beb | -15.2026 | -47.50855 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aff1341d-4222-39cf-999a-0c9929c7136c | -15.19791 | -47.5162 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ee0f4ed-631d-3046-abde-a600b5cc85a1 | -15.19506 | -47.5114 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e5bfe38-f7ca-3429-9ac2-0b4545dc0e78 | -15.19446 | -47.51548 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 572c7d8d-db91-3ae9-bca8-bf18d57b60a3 | -15.19102 | -47.51466 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c74d5923-49cf-37fc-8f58-f04afb012c4d | -15.08553 | -47.17937 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40372f77-3856-3111-b186-a64ceccaa9ad | -15.08533 | -47.18068 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 413a1480-7975-3a0f-8e3d-6457b67b60d0 | -15.08495 | -47.18343 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d26f8c60-3f24-30a0-8686-38dd83651ab8 | -14.80036 | -48.03775 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd028b6d-c197-39fe-8907-4a7a3f8ced3c | -14.7998 | -48.04148 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6316d73f-52e9-344c-aa4b-28c234e022ae | -14.79931 | -48.09116 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 249964dd-b822-3c0a-9b63-986f665c1cd3 | -14.79873 | -48.09496 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d21d131-8a17-33ca-8416-e7dbd871bb2f | -14.79752 | -48.03341 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 621bb478-92aa-3e66-b04f-647a19ca9b33 | -14.79641 | -48.04087 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 36cfb267-44bd-393e-b0a6-3dd06446ae21 | -14.79525 | -48.02534 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 822e820d-d86e-3c94-a686-6ab5b4eebd3d | -14.79468 | -48.02909 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 77a872b1-770a-37d5-98fb-6651ccd54608 | -14.79413 | -48.03281 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ccc6158d-5b59-3288-86fb-ba74ebf36614 | -14.79374 | -48.24304 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e159ad6a-5a1d-3a71-a48a-b55b1d4c866b | -14.79301 | -48.04026 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 263b5ad1-92d9-3c43-8272-ba7cca8b0624 | -14.79244 | -48.04403 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c77f6ffb-4dd9-3c14-bafc-09a47c462585 | -14.79188 | -48.04779 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 384677c3-b9ba-35c7-99b3-e7d5dd79ca56 | -14.79184 | -48.02477 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe4c7562-29ca-373c-8933-c12c5a068c31 | -14.79129 | -48.02849 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7135bea0-96c4-36b3-9c91-25cfab03a758 | -14.78855 | -48.09318 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e165b7e4-4510-3253-a6b1-7560284d0e0a | -14.78848 | -48.0472 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f65b521-b358-3c8b-ab98-d9d52e0ecef8 | -14.78792 | -48.05093 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0df2d072-015b-3865-9628-5e376e2f7173 | -14.78789 | -48.0279 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 91c04941-8fbc-3215-9979-9e815c38c55b | -14.78733 | -48.0316 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bd9e3788-e4eb-31f0-8bca-464a77048680 | -14.78452 | -48.05035 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c90c3d04-d3c6-34ba-b9ac-639d4e8b4a4a | -14.78448 | -48.02735 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8982a49d-272f-3be0-9de4-71aad874d930 | -14.78397 | -48.05408 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 089fa09b-61ea-3f8b-ac72-9481fc63f743 | -14.78392 | -48.03106 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 51a88a5f-6e0a-3793-b09c-b3f116c5c125 | -14.78337 | -48.03476 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8ae944a-c20f-3699-bf05-f68de162690a | -14.78107 | -48.02681 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5f0925ee-832f-3ae0-b9bd-3564e5dda96f | -14.78066 | -48.09936 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d06112d-42b9-301c-a6b7-6a0017954ccb | -14.78057 | -48.0535 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2ebb5c4-d567-31c6-9f35-9cca92f6e295 | -14.78052 | -48.03052 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 971216fe-3f46-3784-be7f-1c7ab370cd5a | -14.77997 | -48.03421 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7c93724-f026-3694-9da6-d364b492b475 | -14.77941 | -48.03791 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e94c8853-2576-3a02-87eb-0d0d27d119bf | -14.77782 | -48.09506 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93da6f2e-b987-31b7-9de9-c2523fc570ff | -14.77767 | -48.02624 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad4c7d97-a558-392b-ba38-6413a308fd64 | -14.77711 | -48.02995 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1b7532f-d4a5-3da6-ab0a-ba6025f63138 | -14.77656 | -48.03364 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cbd7c51a-2e62-3d7f-bc02-242efd2607c6 | -14.77601 | -48.03734 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2f0371b5-47d6-3dfe-b2d5-3f2dd54ea0df | -14.77372 | -48.02935 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e584742-161e-3a2d-bf4d-71e078654378 | -14.77316 | -48.03306 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8373f248-af68-34f7-934e-b717687b6f13 | -14.77261 | -48.03677 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0d6c8998-03ce-3410-af0e-4ee084c8d1ee | -14.76976 | -48.03249 | 2024-10-04 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc0a1c59-e27f-34c6-8e16-f64e1c21a8c0 | -16.09383 | -47.93217 | 2024-10-04 04:34:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76b4903f-52ec-3830-8bca-cce2003c3d0e | -16.04685 | -48.52903 | 2024-10-04 04:34:00 | NPP-375D | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 02cfd423-6741-387e-8f59-d2c98e72d0bf | -16.00941 | -47.81902 | 2024-10-04 04:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fcea0da2-9a09-3841-841a-da6b61a74879 | -15.80035 | -48.15184 | 2024-10-04 04:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a5459409-e47c-3c74-9f80-e911c52f88b8 | -15.70588 | -47.80336 | 2024-10-04 04:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38752a7a-4d45-3236-8576-f62fcf94fde1 | -15.64797 | -47.72724 | 2024-10-04 04:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc6843a0-69b9-3009-be17-3efeb7038bfc | -15.62464 | -47.20025 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad3e66a6-887f-36ab-98b5-5d90254a98e3 | -15.62247 | -47.19662 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6107d8f-302c-395b-834a-b210dfb8898b | -15.62186 | -47.20071 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc82728c-c212-33fd-ba3d-0b6bb63c3d72 | -15.62169 | -47.19557 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b063a76-c6c5-30e7-8b4b-e780fbdec78a | -15.62111 | -47.19967 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b9a48aa-2acc-3617-b14f-0b2c67f89fae | -15.61893 | -47.19606 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bbc99869-d304-3d28-8e49-03c9a5919f54 | -15.61833 | -47.20016 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 432449f9-23eb-355e-b5a6-924f7dc867d2 | -15.61479 | -47.1996 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff42d031-f487-3d4f-b0c0-c3b57fcf2977 | -15.61419 | -47.20369 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71a8f546-f8c7-3693-96a3-74d4be8f0e0f | -15.61359 | -47.20778 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 373f2b79-c9ea-356b-bf4f-9b030951044c | -15.41021 | -47.41703 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2ae2829-bd91-30b1-b8f0-7d5cf75306cc | -15.40733 | -47.41225 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5c940dc8-9636-364c-aa1f-770ad3a3cd74 | -15.40382 | -47.41174 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1bb89ce-f016-30f3-92f6-264d26bcdf98 | -15.40322 | -47.41593 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9a03fbef-0ea3-3d5f-b0ae-c93e0dcabfe6 | -15.39915 | -47.41928 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be6dfc22-ee30-3533-bb3f-688907b58afc | -15.39509 | -47.42264 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bfb5fbc3-2457-3824-9584-5b4dacf89d6a | -15.39162 | -47.42187 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5b42801-8c32-3ec9-89fa-826731961ee7 | -15.38815 | -47.42113 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b437ed4-c3ff-3fa3-9bb0-9ae5e9fdd2a7 | -15.38059 | -47.42397 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9548e813-8c67-379c-abca-7f73aaba80bb | -15.27598 | -47.50221 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8f9bd76-41ae-3023-84f5-466c6cd43ac7 | -15.27186 | -47.50605 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69125230-947d-364c-80df-60ebf3f01991 | -15.26898 | -47.50134 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fba3128-33d7-3467-9819-ea1025734fb2 | -15.26836 | -47.50566 | 2024-10-04 04:34:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README119.md)
