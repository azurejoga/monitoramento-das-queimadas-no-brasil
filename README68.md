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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3fffea0-ace5-31c5-9530-1c9624789e6b | -10.72936 | -47.73313 | 2024-10-05 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 319e6387-48af-3a56-a6f0-00b3258808ea | -10.72859 | -47.73769 | 2024-10-05 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19f3dda7-56e9-3e28-8231-043ef33425ad | -10.72781 | -47.74233 | 2024-10-05 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04ba4072-3832-3f0d-8195-76eeac1319ae | -10.7264 | -47.72795 | 2024-10-05 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6bb0436-8359-3e0d-8f16-7760ffda7814 | -10.72563 | -47.73249 | 2024-10-05 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96137ec1-09be-35d4-9d4a-76fab353e33d | -10.7248 | -54.20544 | 2024-10-05 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99fce08f-1cd8-34e4-8920-8ecf58a2d86a | -10.72406 | -54.20929 | 2024-10-05 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e529a6dc-ae7c-3e8d-b164-b3b32f70f366 | -10.72342 | -47.7229 | 2024-10-05 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18a41a23-f5be-3692-987d-d1a33331dccb | -10.72267 | -47.72733 | 2024-10-05 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cbae46db-a775-355f-b03a-81b0eb695fb9 | -10.7219 | -47.73187 | 2024-10-05 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ec0774b3-5064-3f3a-87a1-faa18ef25788 | -10.71969 | -47.7223 | 2024-10-05 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4464f333-2f1c-3b36-8f37-f3342f8a5eb5 | -10.71894 | -47.72669 | 2024-10-05 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb591798-e1ad-3149-b788-a48fb4aec464 | -10.71818 | -47.73115 | 2024-10-05 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 86b6d59b-fc94-3010-a791-43d4f2293fdf | -10.71596 | -47.72168 | 2024-10-05 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f129107c-63b9-3add-a3ab-6baac7cc26af | -10.71522 | -47.72602 | 2024-10-05 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e09b8ae-47f9-3e7b-84a6-9e3b48b68fcd | -10.71447 | -47.73042 | 2024-10-05 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85cea5eb-a635-367f-90a6-171f16ad2b6f | -10.69393 | -48.72071 | 2024-10-05 04:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 55afe46b-93f3-39b4-bd13-91cd93541c53 | -10.69302 | -48.72611 | 2024-10-05 04:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62adf3e5-d6db-31fc-b816-051fb212e9eb | -10.68921 | -53.04074 | 2024-10-05 04:14:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e99339e5-24e3-3043-b833-45898c6c114b | -10.66782 | -50.68667 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d28ecc73-5ff9-37f2-8b83-aa2322a2e7a4 | -10.66702 | -50.69122 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2eb45f47-40c1-3e16-bf16-6bcc79cbe042 | -10.66621 | -50.69578 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e01654fb-fa7b-3083-af53-977555f8fcfa | -10.59849 | -48.05244 | 2024-10-05 04:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d80df51c-f7b6-32fd-9b99-bcdcc2a3939c | -10.5947 | -48.05171 | 2024-10-05 04:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7d7baefd-30f8-3aaa-b724-1e3f2fd3a7be | -10.59089 | -48.0511 | 2024-10-05 04:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e66d2af3-7026-3926-a17d-0bce2cb41784 | -10.5421 | -46.2788 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75877e5d-7060-3dd1-98c2-2a09d98579aa | -10.53862 | -46.2782 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c25f6ba0-d2e0-3a9a-8042-562fe5c0b0a7 | -10.48678 | -50.25683 | 2024-10-05 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 867becc3-f9e7-3b0f-8c57-61238c2d35fd | -10.48602 | -50.26112 | 2024-10-05 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09aa5eae-2d60-3f1b-9735-b08e51b9c115 | -10.46292 | -50.72859 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 455890d0-916d-380c-ad9b-39c984206f0f | -10.46109 | -48.34696 | 2024-10-05 04:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f5555d65-6b92-349e-9f4b-e9ac6000a85b | -10.46078 | -48.34468 | 2024-10-05 04:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8a3a5102-b0ec-319e-94a8-8fe5f9e338f5 | -10.45841 | -50.72773 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d24f4bef-6dc8-3e20-b4f5-698c7812e5a7 | -10.45722 | -48.34628 | 2024-10-05 04:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ad4abd06-f2ea-3b65-9501-dee617521b21 | -10.45691 | -48.34399 | 2024-10-05 04:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1b4aedfd-0cd6-35da-8b13-93aaf0c5c14f | -10.45608 | -48.34893 | 2024-10-05 04:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9fafd684-cfc3-3e9a-bd1c-1f6b9cde1004 | -10.45389 | -50.72689 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f710173-6734-3e99-a0b7-71f184f19ee6 | -10.45309 | -50.7314 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9da6370b-b850-30d6-8fce-e8ad77d0815c | -10.45015 | -50.7216 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c5b8004-3331-32f3-9e8d-e6b2900112bb | -10.44935 | -50.72613 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f422c1a-fd97-3436-a782-8d1cb381af61 | -10.44855 | -50.73067 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37ede531-2fc8-39c9-895a-3d01173ac47e | -10.44643 | -50.71624 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| acaee9c6-d703-3ad0-9cdb-fa382d3882f4 | -10.44563 | -50.7208 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f958ff7-2405-3f4a-9c43-021ee0598165 | -10.44482 | -50.72535 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 46b37573-00e4-3c8a-a117-45bb49d3034d | -10.44401 | -50.72991 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 668041b0-69a0-3434-80ea-709116aadb83 | -10.4411 | -50.71997 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d63198fd-7f66-3a63-9100-e4f6d9f5ea5d | -10.44029 | -50.72454 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 865ee83f-3cce-3594-8bcc-10b643e7082e | -10.43948 | -50.72911 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ae99380-d57b-3f6f-b183-9e4440dc1941 | -10.43867 | -50.7337 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 046d0ff1-d6b4-317f-86d4-60e6bff56a7b | -10.43831 | -50.7621 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9902e32a-25a3-3c50-87fb-8fa3c27ca61c | -10.43786 | -50.73827 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ea512436-3f60-383b-a809-9be64f341628 | -10.43748 | -50.76678 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 386ad045-9174-3f89-aa0d-e1120a43b063 | -10.43495 | -50.7283 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6ca0e780-806e-352b-ba66-731ec40c4e1a | -10.43414 | -50.73288 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 89117b53-8c53-398c-b59b-9ca2690abf3b | -10.43376 | -50.76133 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f30f2f9a-c66a-3720-adfd-ef7de2a10438 | -10.43334 | -50.79016 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4506193b-569e-3e10-b4df-b4fcf77e221c | -10.43332 | -50.73747 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d1c9a87-ce90-371a-b470-b91de3617e4e | -10.43294 | -50.766 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23cdc172-a8ee-3f59-b38b-0f603d3b1dbf | -10.42961 | -50.73206 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 79d363bf-a594-353c-9d5b-f0582fba9b28 | -10.4288 | -50.78931 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4fdc493a-4d40-334d-bc24-3406300e67d1 | -10.42879 | -50.73665 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09ee5369-f633-3847-8ad3-f2ecd75d9433 | -10.42797 | -50.74127 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e1b298a-f1c9-3f2d-88ad-a0055be6a86f | -10.42426 | -50.78846 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ea23a9b-228b-3449-a87f-d9c20f7a1c73 | -10.42264 | -50.79755 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5d57ccbc-c069-3c4c-a279-2ffc5762fb3d | -10.41726 | -50.80135 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 018da26a-9a7c-3997-a11b-c14274481e6f | -10.41643 | -50.80605 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c37a2fcd-8116-3b89-b84f-c2db06b82292 | -10.39368 | -54.80415 | 2024-10-05 04:14:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7edba666-0b6b-3fcd-98a9-22799de913d0 | -10.39285 | -54.80841 | 2024-10-05 04:14:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9290e3d7-c79f-3a7d-a0ec-b17bd37a835e | -10.32795 | -50.54129 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4b206f5-48d5-370e-a891-2a2b8fd8cec2 | -10.32714 | -50.54578 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd8c897c-13bd-34bb-9360-fdff88940677 | -10.32634 | -50.55028 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80d67d2d-ee89-3402-8fe1-2d8f0235d950 | -10.32589 | -50.52702 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 285ea8aa-3ed4-30da-bafd-97488e343a2f | -10.32508 | -50.5315 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1f8c351d-fa0e-3798-a389-3d151799262c | -10.32428 | -50.53598 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2a96b53d-3153-33e1-9ec7-8adc68505673 | -10.32384 | -50.51276 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 5226fc22-e630-34d4-b0ed-0ae9d3173217 | -10.32303 | -50.51724 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 1c2b32a4-113d-3c8d-afaa-1494fd91c531 | -10.32267 | -50.54496 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 39c972ef-78af-33fe-a337-cffc2665b4af | -10.32223 | -50.52171 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| cf2b4c1e-8164-327a-a30e-46056639005b | -10.32186 | -50.54946 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1a8d06a-5933-34eb-b7f5-645984a0a51a | -10.32142 | -50.52619 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d4249947-53ce-311f-bcf2-4293f1fbc31c | -10.32061 | -50.53067 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 010b85a0-81fb-3fba-b084-6f12168c9a7b | -10.32018 | -50.50747 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 03018720-0ae0-3d18-9cff-cfbe79a16b2d | -10.31937 | -50.51194 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 34.8 |
| b35a102d-a717-3832-8064-64893e64d5b3 | -10.31856 | -50.51641 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 231b476a-c443-392c-b894-4570bc320a8d | -10.31776 | -50.52089 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37fe41ab-e27c-3035-a3d2-67de1809e5ad | -10.31571 | -50.50665 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 57b75888-7d50-309f-a951-0f636a6e2829 | -10.31491 | -50.51112 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 34.8 |
| a6f373f7-d954-32dc-ba5c-5a5ae4401e6e | -10.3141 | -50.51559 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 34.8 |
| a01136b0-2797-30df-8794-ad2e8305536b | -10.31329 | -50.52007 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfecedf8-7abb-377a-a575-898cbad7c423 | -10.31248 | -50.52455 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cd50984-9e36-3a95-8568-58070a327845 | -10.31125 | -50.50583 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd112203-efa3-316c-8fbc-029536ee5076 | -10.31044 | -50.5103 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c4735277-77a6-31df-8d50-bfb5326b6ec7 | -10.30963 | -50.51477 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0850bcdc-fc6f-339b-8c1c-0b4ccd8f5ca1 | -10.30882 | -50.51925 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3bd9f8fa-aded-384c-b737-4c544ad045bf | -10.30261 | -50.51566 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| baf7f087-e3c0-3df2-ae95-e7187bfd703c | -10.30191 | -50.53187 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c2027bf-bb9a-3553-bfc8-2153a219d285 | -10.30183 | -50.52014 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6b93cd10-3ad5-3e9c-9e58-16d8531487e7 | -10.30105 | -50.52464 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7d6ed155-8e01-3310-993f-2cb1aba6bb57 | -10.30069 | -50.51313 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02987af0-74e5-36cd-9c0f-b0585f9b7fe0 | -10.30027 | -50.52914 | 2024-10-05 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README69.md)
