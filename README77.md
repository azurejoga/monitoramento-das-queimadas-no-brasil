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
| 9f68f996-c4ce-3f1b-b050-f80b3de3d236 | -3.93699 | -46.44963 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ed0a5df5-49c3-3417-b4c2-d910a116c6e5 | -3.93626 | -46.45418 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fff8f61d-6dc4-33f9-b68e-ba9a03bf0f29 | -3.93251 | -46.45356 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 49e159dd-b105-3b10-aab3-541536e9479e | -3.93176 | -46.45825 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 18a8e699-6e66-3ebe-b788-399db1b184b4 | -3.92258 | -46.41968 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18214031-70b6-34b8-a8d1-4f0ec1792b0c | -3.91292 | -46.43188 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0558488c-8737-33ed-b5a5-ece974466cb1 | -3.90853 | -46.45907 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| e8b62e2a-2359-3f33-b35c-939735c03497 | -3.90477 | -46.45851 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 50ac4348-d72d-3e5d-ba96-b34047bed552 | -3.90102 | -46.45789 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c66a41d5-8f02-3df6-b23b-3a371e21b55e | -3.90029 | -46.46239 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| e87b1578-e771-3752-ade5-c19e5e2b3167 | -3.898 | -46.45278 | 2024-10-09 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| a9969904-96a4-368a-bbd1-8b2f8dd6f706 | -3.813 | -47.49049 | 2024-10-09 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e48b8306-ae2e-3853-b503-4669f99983f7 | -4.7384 | -46.66076 | 2024-10-09 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce157f66-0aca-31e4-bb22-49b5e902253f | -4.52858 | -46.61289 | 2024-10-09 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad954287-bae3-3e50-bd65-6354853029e7 | -6.44524 | -47.05907 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0e95a44-faa6-3d56-8c38-ba1f359c5e76 | -5.76185 | -46.57796 | 2024-10-09 04:14:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa1ef0d1-c909-3fdd-b50b-c081dbedbc2d | -5.55954 | -47.03393 | 2024-10-09 04:14:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c907ee86-bcbe-3a89-8d55-14822019f7cd | -5.55755 | -47.46544 | 2024-10-09 04:14:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f5386556-0e49-3cfb-8bf2-c4bd5fb41b6a | -5.55574 | -47.03333 | 2024-10-09 04:14:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 165f13d0-e200-383c-9a2f-c8ce3e3e7c52 | -5.35126 | -47.69028 | 2024-10-09 04:14:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06be5cb9-18a7-3b68-ad95-8103e68530fb | -5.3507 | -47.6937 | 2024-10-09 04:14:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99b4749f-a0e0-322c-9353-0378324ad162 | -6.11138 | -47.03384 | 2024-10-09 04:14:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 72df9282-1744-3150-8684-15933cfad760 | -7.76495 | -47.04497 | 2024-10-09 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e8dd0e19-94d4-3f7e-82d5-d3a6b9730197 | -7.76423 | -47.04934 | 2024-10-09 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c39f7ff3-ca7d-3e5d-bdc3-dcf070f036dc | -7.67821 | -47.31598 | 2024-10-09 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 096c5207-3182-311f-a102-5b10f34f2bb1 | -7.67445 | -47.31538 | 2024-10-09 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 72a21fff-bef5-3171-ba6c-4ebce4cacd15 | -7.48507 | -47.58611 | 2024-10-09 04:14:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 073b194c-e796-33b8-a501-c24eceac96c0 | -7.43095 | -47.35368 | 2024-10-09 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47169615-6f0f-31d8-98b5-a0eb13b581b2 | -7.35541 | -47.10956 | 2024-10-09 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a52610b6-3bfa-3d28-99ff-3c5a72d4646d | -7.35169 | -47.10892 | 2024-10-09 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bdf38492-5d19-3fae-9e1d-c78a6b00dbf0 | -7.68271 | -47.31205 | 2024-10-09 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ff950076-81f6-3030-bbec-9fd3b2f76687 | -7.67897 | -47.31141 | 2024-10-09 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f42e93e2-7ed1-3179-a13a-5702e024a7f9 | -7.48426 | -47.59088 | 2024-10-09 04:14:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b640e54-4a11-3b35-85be-b196004d4e62 | -7.46136 | -47.54556 | 2024-10-09 04:14:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1f9745f-58fb-38aa-8666-071a2cb0ffb2 | -7.43542 | -48.36054 | 2024-10-09 04:14:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61ceacde-e82e-30b0-a9f7-c689eefad187 | -7.41584 | -47.87021 | 2024-10-09 04:14:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b138512-09f4-3f52-af1c-8934a09d453e | -7.20655 | -47.69953 | 2024-10-09 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 39e051a2-04e4-35e3-bd96-267a17ffce6a | -7.05037 | -48.05991 | 2024-10-09 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92e4824a-30fd-3177-824f-95a512e35ba0 | -7.04641 | -48.05925 | 2024-10-09 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c988b5b4-a072-33f3-a565-a5a24bfd30d0 | -6.96623 | -47.39114 | 2024-10-09 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2063f47-a6c1-393d-b5a6-6099d98a4bfa | -6.941 | -48.17564 | 2024-10-09 04:14:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 835a1240-861a-316a-acca-737c30c316a7 | -6.93898 | -48.17502 | 2024-10-09 04:14:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e6dcfea-d467-3e3e-8233-16d458a5fc40 | -6.85159 | -46.93351 | 2024-10-09 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58bf1a0f-997a-340c-a253-d2666594f7e9 | -6.66687 | -47.10556 | 2024-10-09 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1bb8df4-1278-3d5d-802b-4815a89d2338 | -6.65861 | -47.10893 | 2024-10-09 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aae3d672-defa-3bfa-8579-620c3a1bd433 | -7.01168 | -47.37278 | 2024-10-09 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89cd2863-716a-3c2b-bde5-cf9f7e2d41d5 | -6.96591 | -47.38964 | 2024-10-09 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28400a67-705f-3162-91c1-6c681a37be81 | -6.7295 | -47.2227 | 2024-10-09 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9bf151e-032c-3ef2-be50-2f388809d9cf | -6.67063 | -47.10614 | 2024-10-09 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6f79bee4-49c8-3df4-9273-6fddeeb316b9 | -6.66311 | -47.10498 | 2024-10-09 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 054597ee-a168-3515-9685-54f279729a91 | -6.66236 | -47.10955 | 2024-10-09 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be1a0d08-e1e4-3e19-b231-4a9c0b6c3a1b | -6.62483 | -47.07988 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 507b9a2b-4b4b-3c3c-932c-8b74c9cd9d6c | -6.62408 | -47.08442 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1dce82a-9012-3de7-8215-bccd29e65c45 | -6.62108 | -47.0793 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71b99c93-b697-3f6c-8dd7-a4aa879801e9 | -6.62032 | -47.08385 | 2024-10-09 04:14:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77240393-518f-3cd0-9054-d0e0b1966a0b | -8.49707 | -48.63816 | 2024-10-09 04:14:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 0b7ff3b7-cef8-37d8-997b-56246d2e5312 | -8.49432 | -48.63799 | 2024-10-09 04:14:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 478d3771-c084-3218-bf36-882d06f70547 | -8.49305 | -48.63748 | 2024-10-09 04:14:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 17b7e300-5a23-3629-85ec-f8c6809adec2 | -8.32706 | -48.01542 | 2024-10-09 04:14:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bb7ff52-8656-3f0e-9e66-d06d2328264c | -1.84627 | -47.85019 | 2024-10-09 04:14:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 52a52de8-340e-38bd-9033-daffc77f18f2 | -1.23939 | -47.89756 | 2024-10-09 04:14:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f993690d-9b7a-335d-9334-4e3857057ad6 | -1.05834 | -48.00436 | 2024-10-09 04:14:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21118313-8feb-37a7-9ad0-065918853946 | -1.60356 | -47.38337 | 2024-10-09 04:14:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 587ec08f-d256-3b13-a5ac-8638c5e0cf70 | -1.37814 | -47.49041 | 2024-10-09 04:14:00 | NOAA-21 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cac63810-7528-38dd-81c3-a9925786db8a | -1.37755 | -47.49421 | 2024-10-09 04:14:00 | NOAA-21 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea3fc84e-12c3-36a8-9432-1a75346d61c1 | -3.49796 | -48.89642 | 2024-10-09 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a179c4f0-14ae-3936-9ad2-7e254373bb1a | -3.49425 | -48.89137 | 2024-10-09 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f9909a9-aab8-36d5-9804-bd2a9f306cb1 | -3.11664 | -48.63187 | 2024-10-09 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f78ab52e-9e2d-3e42-9b77-b768411165d2 | -3.11595 | -48.63611 | 2024-10-09 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17fa3237-e958-3fea-a585-731b504e8144 | -2.94434 | -48.7481 | 2024-10-09 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3463abb1-4c23-30c7-9634-000c060f49b1 | -2.9442 | -48.74637 | 2024-10-09 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2f566c26-232d-34e6-84b6-b078f8eeedf8 | -2.93991 | -48.74745 | 2024-10-09 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ffeabfd1-4628-3f32-a895-9e4b3f44e933 | -2.79755 | -48.67739 | 2024-10-09 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3fe74770-2cb3-35c0-8b77-02447dbd30ae | -2.79296 | -48.56704 | 2024-10-09 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c8e24902-2f59-32e0-98c6-fd114efa2bd5 | -2.79227 | -48.57124 | 2024-10-09 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4ff812a0-560a-34d5-a5dd-0a5d3e7cb41f | -2.79158 | -48.57547 | 2024-10-09 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f98d4abc-18fc-3f1f-8865-159ab9d9990f | -2.78858 | -48.56631 | 2024-10-09 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ae270466-2441-3e46-874c-de94588c9890 | -2.78739 | -48.09583 | 2024-10-09 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4078e61f-8b66-368d-bb6e-d1a87aaf2f7a | -2.48625 | -48.05359 | 2024-10-09 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be5caffd-f578-3eb7-a37c-fc7ab42fa6e4 | -2.48201 | -48.05289 | 2024-10-09 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 999241de-d2de-3e08-adad-0ced9f279bef | -2.4765 | -48.06012 | 2024-10-09 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d9be6e1-6c23-3f22-a61d-80cf9a4384f9 | -2.47289 | -48.05547 | 2024-10-09 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5737a731-4c20-3fa9-8d12-f71004d830bf | -2.35278 | -48.49608 | 2024-10-09 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1331c40c-06a6-3409-ae64-36996275eee5 | -2.20843 | -48.15991 | 2024-10-09 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4052d4a8-e69e-37fd-800a-1dfea261f2a3 | -2.18544 | -48.82666 | 2024-10-09 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 577d763e-31e0-3418-a03c-2255a7660a17 | -3.69473 | -47.62341 | 2024-10-09 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c9a5aac-d639-305b-8862-a8b794225966 | -3.46306 | -47.65987 | 2024-10-09 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ac592e9f-648b-3fa3-9f65-6266995f511d | -2.53756 | -47.62502 | 2024-10-09 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a80359f8-e0e7-3919-8153-a4e32d1b0ae4 | -2.38519 | -47.6857 | 2024-10-09 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf13c970-2e8b-3b72-9aa4-d8017287eaf6 | -2.38104 | -47.68504 | 2024-10-09 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 863e4b22-bb9d-3459-a96c-9d35d6fb4fe1 | -4.49119 | -48.11533 | 2024-10-09 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 2846e893-ea6c-3cfa-b915-c5aaf79f9b7f | -4.20358 | -48.14233 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa699dbb-aba4-3454-a78d-bb7e6d2b2f1d | -4.10162 | -48.2607 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6fcfd17f-27d9-3d42-8f5c-798a27817ef6 | -4.09973 | -48.25171 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e627a2fe-f009-3fe5-bddc-53336b5833a8 | -4.09908 | -48.25555 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bbddd994-e4c7-3793-bb54-4f14aec8a388 | -4.09868 | -48.25217 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c1fe1cca-5d41-31da-9e6d-f55eaf804dd5 | -4.09842 | -48.25947 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 5414099f-0914-320d-a7b1-cc431f982e44 | -4.09806 | -48.25603 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a014dca6-969f-3724-bdea-7149ed082c0a | -4.09776 | -48.26338 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 093ef6cc-aaba-3622-944b-e923a216a33d | -4.09743 | -48.25995 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |


[Clique aqui para ver as próximas entradas](README78.md)
