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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec922588-9e0b-3561-9963-ebece88bac37 | -2.10226 | -48.36707 | 2024-10-20 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f7081c6-3c99-3fc6-befa-6b625f4e1674 | -2.00566 | -47.96189 | 2024-10-20 04:29:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95171958-0bd5-3219-856d-0487a299dde2 | -1.99501 | -47.94207 | 2024-10-20 04:29:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7aadc3b6-a00f-3f22-b959-ee1932aeba65 | -1.82495 | -47.22402 | 2024-10-20 04:29:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 674cc4ff-185c-35f9-b34e-3810ac05fd75 | -1.50463 | -47.21606 | 2024-10-20 04:29:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e288a5e-c8c8-30a1-a627-b358d340486b | -1.43565 | -48.14506 | 2024-10-20 04:29:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e71d6583-ae7c-363b-8540-cee3d52de64e | -1.41532 | -48.3842 | 2024-10-20 04:29:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 625e0b6e-a382-3739-8824-e41042f6aff6 | -1.12451 | -47.26365 | 2024-10-20 04:29:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63e6a0cf-91a6-3217-9f0e-8e652079b62d | -1.12118 | -47.26313 | 2024-10-20 04:29:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 73956e76-236f-37c6-aa03-6f1cb434432d | -1.05766 | -48.25846 | 2024-10-20 04:29:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa15aa17-db4c-3af5-b2f5-6263724965ae | -1.97541 | -48.68188 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c88b1f8-e8e3-3aef-a92d-44629ad646ac | -1.97482 | -48.6856 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e67d39b-d875-310a-b48b-048a723a0b8f | -1.97422 | -48.68932 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58d076d9-3476-3962-aa94-21dd1b1fa00b | -3.48738 | -48.24397 | 2024-10-20 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0efe4660-420a-3272-ba9c-2fddd7628eed | -3.48401 | -48.24346 | 2024-10-20 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b24a3cdd-a700-3746-a5c7-4f6623ac325b | -3.46355 | -47.66848 | 2024-10-20 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b9cddc94-e22f-317c-b8aa-7a731e465b98 | -3.42999 | -48.82608 | 2024-10-20 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0300715c-9665-34a2-93b7-a48ae21eb407 | -3.25551 | -47.97226 | 2024-10-20 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44198d5b-6832-32a2-a477-16487dc5fae0 | -3.21918 | -48.61338 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 51603dda-feef-3e8f-8f4b-113292b0e91a | -3.2186 | -48.61701 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28a5b2b4-3905-3402-a5c2-2ca283b56493 | -3.21635 | -48.60921 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ec1f20cf-dd19-342b-9f41-36cabf56ae24 | -3.21578 | -48.61284 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5397d7e9-8276-32eb-9a53-bebfc59f0530 | -3.2152 | -48.61647 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bbb11d0-fe4d-3abe-9796-a824ebce1baf | -3.21462 | -48.62011 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9a80668-96f5-3cf6-b12f-778500969a25 | -3.21238 | -48.61231 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8eb6f9d-4fa5-3afe-9744-d913a5757d3d | -3.2118 | -48.61594 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d5b17165-7da3-35e2-960f-8a4c7e846327 | -3.21122 | -48.61958 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9eb6d729-4eae-3c15-9754-c769a9225626 | -3.20898 | -48.61177 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09401d6b-01be-3c86-ad43-cb4ded191010 | -3.2084 | -48.61541 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 09436eb7-cc4b-3c39-9862-b1d1e30c4da7 | -3.205 | -48.61487 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 816753c0-93d1-3413-bd0f-1037c5a3514d | -3.16371 | -48.36869 | 2024-10-20 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e7818de-2ee0-3a7a-8ebb-146ac5fabb29 | -3.16315 | -48.37226 | 2024-10-20 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a465089-3cf5-37a7-aa99-321b735f342c | -3.15977 | -48.37172 | 2024-10-20 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d71afc04-3eeb-3e32-b9f5-93f2ff4d918c | -3.11186 | -48.63059 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2aa6032b-3819-3704-a99a-95532339b6ff | -3.04854 | -48.01955 | 2024-10-20 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a7b429e-3cf7-32a4-9d4d-5a61b97d4f1f | -2.97387 | -47.91731 | 2024-10-20 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 75a3ba5b-056e-37e2-b153-675ad9a260d1 | -2.30387 | -48.59171 | 2024-10-20 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0202c803-67a1-3d7f-9229-3fad735ceaf8 | -2.30222 | -48.58017 | 2024-10-20 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 703455c8-b324-33fe-b2ab-077cc1b713a5 | -2.30163 | -48.58384 | 2024-10-20 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 45ba3a59-27b7-3b5b-90e2-ee8a1f1df5db | -2.30045 | -48.59118 | 2024-10-20 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5135b093-bbbc-38d5-9929-8fde76f38d75 | -2.2988 | -48.57963 | 2024-10-20 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 5a3b04a5-7a41-3bd1-b410-3bdb189b3d6f | -2.29821 | -48.5833 | 2024-10-20 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| a3f1f13b-acd2-3dfd-a51e-640bad8e4d32 | -2.29762 | -48.58697 | 2024-10-20 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4dee569a-8ca9-3a2f-a1bd-711ffeb1dd36 | -2.29704 | -48.59064 | 2024-10-20 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ea90e7ca-fb67-388f-9cc2-cfa1c191fe80 | -2.29645 | -48.59431 | 2024-10-20 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95658389-c140-3e33-a112-3543a5dc6431 | -2.29362 | -48.5901 | 2024-10-20 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9498fcbb-f47b-3b1f-93f6-fa473b81f200 | -2.29303 | -48.59377 | 2024-10-20 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6c9d0dfc-cb5f-370e-b6fa-c75dbe1bdb45 | -2.18668 | -48.73673 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b1927d4-c082-35e8-a80a-6e9c3e89f429 | -2.18324 | -48.73619 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8b66a75-63c1-3f80-8273-65c631de65e5 | -2.1798 | -48.73565 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f6ca76c-379a-333d-baed-998a621a8a50 | -2.85284 | -48.61244 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f24f55da-086f-3879-b7a4-03e93acd4878 | -2.80298 | -48.68372 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7bdab475-7bd1-3071-bbaf-2ceb081c3248 | -2.80241 | -48.68739 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 247fe79b-0c2a-36f7-8c95-01ca210502e5 | -2.80015 | -48.67951 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6be9bb0f-d680-38b0-9d71-eb3a178d5edd | -2.80009 | -48.70208 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac73c816-6c62-3ac1-8a8d-9fe7d69ccc76 | -2.79957 | -48.68319 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5e014ed5-1f57-398b-b487-e5f46733cfe7 | -2.79899 | -48.68686 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d189a5b8-9e3a-3601-a903-d5e3b03c0f37 | -2.79673 | -48.67898 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 4cfede6a-af97-3811-ace0-f69c11e1bf65 | -2.79615 | -48.68265 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| cb8bfd54-03aa-3154-aafe-80f185b78411 | -2.79389 | -48.67477 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2ebdd4d-2371-3038-9ee7-36983c94c590 | -2.74091 | -48.6777 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e993cc9-a1a1-3f12-ac33-d69ff6800c8a | -2.74032 | -48.68137 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2adf275-b4f0-38df-8921-e8d8b958f885 | -2.7369 | -48.68083 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 662e1202-441b-39ce-8ffc-61632bd0fad2 | -2.73349 | -48.68029 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06cac0fc-ebb8-3148-9bf3-9d6aa4145281 | -2.73183 | -48.66875 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4c0772e-e7d8-3e94-99c1-b27898f6025f | -2.73124 | -48.67242 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91c37013-7ad2-3436-8cfb-279952a1b5bd | -2.71958 | -48.83329 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f22ee298-9085-3213-9d7c-2f0ec09cbe65 | -2.66416 | -48.54646 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c460a148-df40-3712-89d5-f340d906d2b7 | -2.62787 | -48.53329 | 2024-10-20 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32d4109e-306f-34dd-b1fa-702399667bad | -2.4408 | -48.50113 | 2024-10-20 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bdd591d-e8bf-3c65-befa-2273dceb3e5f | -2.44021 | -48.50477 | 2024-10-20 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64f00cd6-556e-384c-a485-6127bc931443 | -2.43755 | -48.45589 | 2024-10-20 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90203921-347c-364d-a28d-b4b30e3c4312 | -2.43739 | -48.50059 | 2024-10-20 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2f1f7aad-accb-377b-b1dc-8f02ed78a46b | -2.4329 | -48.48497 | 2024-10-20 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d9e66db-fcde-30e3-95b1-a6274d148f7d | -2.43232 | -48.48861 | 2024-10-20 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e41e295d-197a-3683-a606-ddaf8b50b8d3 | -2.4295 | -48.48444 | 2024-10-20 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f24830db-932c-39ae-9afa-fa1092ade5fe | -2.42055 | -48.45322 | 2024-10-20 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b0ecafe-67b5-3472-9a8e-56fc09482a88 | -2.42022 | -48.45281 | 2024-10-20 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28603260-2d32-3202-9197-dd15e61a3f2b | -2.41865 | -48.88354 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abbb2e42-fe01-361f-8073-71af8c1327ee | -2.41681 | -48.45227 | 2024-10-20 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99815916-5b6e-3a33-8018-d3348e4c127f | -2.4152 | -48.883 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d50cd5f6-af15-3caf-89a4-782d5ee4bd2d | -2.3654 | -48.60135 | 2024-10-20 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4db711b3-03f4-380f-89b7-1c1c8cca99ea | -2.34704 | -48.80703 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0e0f310-0c34-32e8-be59-d5a74cdcf7cb | -2.34083 | -48.44778 | 2024-10-20 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a01f19d4-7014-3d81-a8a0-075e6907986e | -3.25496 | -47.97577 | 2024-10-20 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d799722-997f-3757-a805-9251e62272cb | -3.0491 | -48.01602 | 2024-10-20 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 646382d4-9fd7-3a8f-bf65-b4dd7e4f5b40 | -2.97721 | -47.91784 | 2024-10-20 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c84fd20e-6598-33da-aa1f-eb21b1930aa6 | -2.51765 | -47.48469 | 2024-10-20 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 119a0376-ad1c-32a1-8631-8e2c5ab6d6f7 | -2.5171 | -47.48816 | 2024-10-20 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 066556cf-fac2-32bb-b28f-5e83d2355593 | -2.51432 | -47.48416 | 2024-10-20 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9c3a4a47-c5ac-3fc1-a852-2734d3241f6f | -2.51377 | -47.48764 | 2024-10-20 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6bbcec0b-7499-317f-8401-bbbdb8fe82ff | -2.5024 | -48.31045 | 2024-10-20 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1ac0d09-08a5-3308-b935-b3fcb19ad60c | -2.50183 | -48.31405 | 2024-10-20 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 106226cb-08cc-3c57-b6d1-504ae4f92793 | -2.49902 | -48.30992 | 2024-10-20 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2500d8e6-f4ae-3be8-8b0b-70f7c17e8fc7 | -2.46468 | -47.84155 | 2024-10-20 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92ba577e-fa0c-348b-9f5a-0fc4315776c2 | -2.46245 | -47.834 | 2024-10-20 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ea9acda-1fac-3507-b518-d1f74ee5746f | -2.46189 | -47.83751 | 2024-10-20 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e3a58b3-2db8-308c-b586-6e4ae9ec27a2 | -2.46133 | -47.84103 | 2024-10-20 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab4b4b05-a99f-31bc-b2d7-09aca1926210 | -2.36898 | -48.29279 | 2024-10-20 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a1fee6e-24d7-35b2-8755-2b4bd4775e3c | -2.3656 | -48.29227 | 2024-10-20 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README28.md)
