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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1503bdf-fe17-31ed-b6af-c11d53588c38 | -15.8673 | -51.8303 | 2025-09-10 00:30:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 1627c963-c410-3250-a1ab-02962d048967 | -9.0739 | -45.7562 | 2025-09-10 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 8ad2ce8a-043f-3b95-99e0-23dad8718b2a | -7.7893 | -46.0667 | 2025-09-10 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| eb7b12b0-32e2-39bb-afa4-eea26c3eaa75 | -6.871 | -47.8911 | 2025-09-10 00:30:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| dd726565-f8f8-3bc2-ab5c-7b2a50b0e94a | -12.9286 | -54.7949 | 2025-09-10 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| f7f24465-28ca-34f8-9ef5-ce5d226c2bf5 | -9.4388 | -46.7052 | 2025-09-10 00:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| de15e4d8-ddbd-3d93-8f58-5a4341948c1c | -15.8677 | -51.8087 | 2025-09-10 00:30:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 4344f3ba-108c-3dad-ab7e-55a01c2d8dc8 | -13.2031 | -45.2834 | 2025-09-10 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 51.9 |
| c08217e7-a1eb-3729-afc0-4c0f93f0e5c8 | -6.8899 | -47.8679 | 2025-09-10 00:30:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| d5fda33f-59a5-35da-8e91-6a18359a5866 | -23.758 | -51.8917 | 2025-09-10 00:30:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 60.8 |
| 6ab6a7fe-13f2-3b7b-8d76-7890bfdcf80a | -5.7369 | -47.4681 | 2025-09-10 00:30:00 | GOES-19 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 8af5d578-69cd-3f1f-b32c-11c9337ff2bb | -5.66 | -43.344 | 2025-09-10 00:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 147df196-1873-3b03-827a-42199975c16a | -11.3202 | -46.5218 | 2025-09-10 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 598342a5-2a30-338a-88dc-b08431eeafa3 | -10.0157 | -51.6821 | 2025-09-10 00:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| cfcf5f3a-dd43-3bd2-a2f6-7533e637f083 | -6.8897 | -47.8897 | 2025-09-10 00:30:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| fb614428-d007-32f5-bbb1-b7ce3f334d4e | -13.1367 | -54.9171 | 2025-09-10 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 13de09aa-9050-34d3-90e2-3d11a5ee70f7 | -5.589 | -45.0505 | 2025-09-10 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 41763f30-d9cb-324c-8be1-42769ab40597 | -13.1176 | -54.9191 | 2025-09-10 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 8c258494-3d7f-302f-a422-b08240eaae8b | -6.8712 | -47.8693 | 2025-09-10 00:30:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| f04d31d0-267b-31c8-9e5c-476bc3816058 | -14.40071 | -47.51036 | 2025-09-10 00:30:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8aadd420-140c-3f93-8289-19a601600116 | -14.38345 | -47.31672 | 2025-09-10 00:30:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 3fab26c5-11e7-391c-8a5c-74bb44a7eabe | -12.50231 | -45.28475 | 2025-09-10 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8b643f14-d181-34f1-b46d-a4033267f939 | -11.12301 | -45.11821 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| dfa91ec5-70a9-36d2-95ce-567c758567d4 | -12.18624 | -50.64213 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 63ba29cd-f11d-3434-ae10-d66b91839199 | -12.41043 | -47.50802 | 2025-09-10 00:30:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0afa468f-ab7a-3a12-bd65-5b1684711293 | -12.18468 | -50.63017 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| c09bde90-5f9e-3a0e-bb6b-6279b7a1b98b | -15.01282 | -48.02657 | 2025-09-10 00:30:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 2b37e62c-269f-3a83-b5cb-a0c5733ea447 | -11.45086 | -43.66857 | 2025-09-10 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| f0c95111-752f-3d3e-a2a3-63519008b9d8 | -13.90249 | -47.97945 | 2025-09-10 00:30:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3f114738-756a-319d-990f-5afb24be5520 | -15.51249 | -52.77165 | 2025-09-10 00:30:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 8aa18143-a8ff-32b8-996b-75ade83285c9 | -13.7596 | -43.61876 | 2025-09-10 00:30:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 87774183-99ab-3022-ae92-8a90cf6d396b | -11.4293 | -43.59597 | 2025-09-10 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 787606e2-574d-32e6-ab12-7a5251edfeb7 | -13.82505 | -43.85372 | 2025-09-10 00:30:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 07f5268a-ff6b-3de7-906b-723a658dc171 | -13.86717 | -44.46663 | 2025-09-10 00:30:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c75c23f6-3c06-3c48-8cec-0c7f0efd9f29 | -12.68802 | -44.9692 | 2025-09-10 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 28c1356f-4845-3994-94bc-34be9bfaa70b | -11.38864 | -43.53802 | 2025-09-10 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ab627536-223f-3f47-a608-e6e6c475552d | -11.43788 | -43.72086 | 2025-09-10 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 40ce7a39-aae4-3b43-9802-0d991eae3f26 | -11.03662 | -46.0533 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 47a3a3c3-5965-32c4-b4c3-039c7a1fd679 | -14.55858 | -48.77031 | 2025-09-10 00:30:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 841b10f8-5606-3517-9ce3-36b519a5b7e6 | -13.19896 | -43.37512 | 2025-09-10 00:30:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 0202a3e0-cce3-3161-8820-2d7ba9575330 | -11.41708 | -43.58513 | 2025-09-10 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| d95ff9db-6fb9-373d-a3a6-83c880952623 | -11.53775 | -47.32429 | 2025-09-10 00:30:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d757e849-f374-3a84-ae9d-04f2f4e2ab58 | -14.55722 | -48.75988 | 2025-09-10 00:30:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c86253d2-b110-3529-8e5c-703296167211 | -13.19949 | -43.36887 | 2025-09-10 00:30:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 0c9f1cba-27e6-3da4-82b7-8b50bf9cb719 | -11.98908 | -47.19098 | 2025-09-10 00:30:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6eca9074-5962-3219-9d5e-aa98e6e557bf | -12.00567 | -50.98989 | 2025-09-10 00:30:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 453ba1b4-74ad-3cce-8b35-279537a52527 | -12.41896 | -44.71972 | 2025-09-10 00:30:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| dc740b38-96f8-3be9-8935-4f3f6b2fa27c | -13.0143 | -48.01588 | 2025-09-10 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e3d6626e-6407-37f1-a8cf-a03be2786a9c | -11.45553 | -43.63002 | 2025-09-10 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| defeb3c8-85a3-36d8-a181-beb9f5da5ce3 | -12.04644 | -51.06152 | 2025-09-10 00:30:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 01b8f113-2707-3281-8ec5-441cb5ee3d51 | -11.42739 | -43.58353 | 2025-09-10 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 5f90251e-26e8-3102-8290-eb16da7194cf | -15.01155 | -48.01701 | 2025-09-10 00:30:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ca2b0b1d-04bf-3309-9417-5a20a8e39662 | -14.09986 | -42.0941 | 2025-09-10 00:30:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 008c9ff8-bffb-3b3c-978e-1dfe0ec61cc2 | -11.75551 | -50.62709 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| bbd3a44a-2f46-30c2-b538-91f9f1e6cdc3 | -14.50924 | -53.94561 | 2025-09-10 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 25.4 |
| f6059ad3-5975-3182-a066-335bf7bfb4ea | -11.68076 | -46.89801 | 2025-09-10 00:30:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ee039b67-030b-337a-9af3-ae5671b9963d | -11.81808 | -46.75531 | 2025-09-10 00:30:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 28351bc6-2a2a-35ef-a11f-dd8ebbb3100e | -13.92993 | -48.2546 | 2025-09-10 00:30:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 54e7a387-8993-342c-bd9a-29a8e42ebafb | -11.83575 | -46.75259 | 2025-09-10 00:30:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 19dfeabf-2178-369b-9db9-7d51892f47f6 | -12.17303 | -50.61957 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 091fa483-57ae-39cd-b76d-39af93d7b45d | -11.14317 | -46.35073 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4e5b2556-3699-33d4-a567-41210ccf4755 | -14.32784 | -47.30632 | 2025-09-10 00:30:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 933ecc94-bbaf-38da-87f0-433e35066fa1 | -14.36573 | -47.31924 | 2025-09-10 00:30:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 33b59342-7aa9-3d00-9f5c-b3be1f111d66 | -12.42354 | -47.80121 | 2025-09-10 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| aecc9b5f-a176-3e99-976b-a5bcbdf7a75a | -13.96362 | -48.23048 | 2025-09-10 00:30:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e171150c-8acb-385c-8cc0-4853cb86934b | -13.93898 | -48.2533 | 2025-09-10 00:30:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 79b70141-ec66-333f-866e-cb9628567ea7 | -11.67318 | -46.90829 | 2025-09-10 00:30:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ec46c6f7-66b3-3171-97e5-6041aa8af5c8 | -11.86105 | -47.53274 | 2025-09-10 00:30:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e5aee65c-b2fc-3da4-8b1e-7e8a5dd01aa1 | -12.02098 | -46.75881 | 2025-09-10 00:30:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 872cc767-e6a8-3958-b988-27b97dcfc93a | -11.67193 | -46.89935 | 2025-09-10 00:30:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2f2b4285-72ef-31cb-adad-9a62e206d261 | -15.0141 | -48.03628 | 2025-09-10 00:30:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 435b035e-f79f-37b1-b56a-a0353ed19d0a | -14.24319 | -46.68952 | 2025-09-10 00:30:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 700abcf4-dcd6-3566-b4de-dbcd39ed3b59 | -13.05402 | -42.32484 | 2025-09-10 00:30:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 32.5 |
| 448bd526-94d1-3243-a76f-9e6d0800f447 | -11.56971 | -44.65836 | 2025-09-10 00:30:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 1c44f648-85dd-3bee-b5f9-ee6f916fe203 | -11.34663 | -46.55099 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f95c69e4-c413-35b9-9ef2-949efbfda3e3 | -13.15814 | -45.28954 | 2025-09-10 00:30:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| f0cb0a4c-886c-30f5-b884-892252f9cba4 | -12.53413 | -45.30991 | 2025-09-10 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 61f87a7a-458a-39f0-8a92-6a25aa2fed59 | -15.10331 | -50.08995 | 2025-09-10 00:30:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 5266ea6f-9a65-301b-9806-fa83c8082f96 | -12.14154 | -44.84473 | 2025-09-10 00:30:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 7026e4e2-8495-3484-822e-05ab22ce6d1a | -13.03343 | -48.0226 | 2025-09-10 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 93e632f3-6f1f-3cf7-99ac-4c68e4266397 | -12.17457 | -50.63151 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| bdf9c29c-2461-39e1-8259-7490bff00d8d | -12.67872 | -44.97064 | 2025-09-10 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c13c7621-c1bc-36fc-ac63-840d9f70dea6 | -11.75701 | -50.63889 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f631f05e-c909-336f-9182-c443d4fb6b11 | -11.37541 | -45.58701 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8e52b659-f2c4-3f50-a7ac-9b842f953845 | -13.82671 | -43.86495 | 2025-09-10 00:30:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 923ddbe1-48b5-3dfc-9bad-2bda590a64c0 | -13.91022 | -47.96884 | 2025-09-10 00:30:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 671c9e2d-1243-3e01-aba5-d4c7063302f9 | -10.60487 | -43.31496 | 2025-09-10 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 7dcde467-98e3-3696-880b-1f06fc781639 | -14.38469 | -47.32579 | 2025-09-10 00:30:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4545ee18-76ee-3159-bb70-fc4849dce48d | -14.9228 | -50.11352 | 2025-09-10 00:30:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 38.3 |
| ec1be9cd-ad2f-3f51-930a-dbcc8635389c | -11.75952 | -46.46803 | 2025-09-10 00:30:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c5e732a6-991e-3e0c-ab58-4f6c00aa7bce | -11.1215 | -45.10784 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| bd114591-9572-381d-b547-e97de26824fe | -12.42478 | -47.81028 | 2025-09-10 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 93e9ef13-d1ec-3754-a830-92cd8a60e9c1 | -14.41085 | -47.51832 | 2025-09-10 00:30:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cd00893d-1acf-31b7-93d9-25f51edd1f2d | -12.44245 | -44.74789 | 2025-09-10 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| be01402b-59db-3e77-9bfc-5fd108e5321e | -12.4205 | -44.73006 | 2025-09-10 00:30:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3e40930c-a433-3c4b-a722-2767683333c0 | -14.37458 | -47.31795 | 2025-09-10 00:30:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 9edd70f9-d865-313b-a65c-a4cde69433ad | -11.32243 | -46.508 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 273d3fac-17e8-3805-b9a8-582357dc44ef | -12.40919 | -47.49901 | 2025-09-10 00:30:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ae7c6b4f-3c9d-3e73-9953-73c2e5dbf08c | -13.82814 | -43.8583 | 2025-09-10 00:30:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 02957c2a-de51-3f3f-9fa0-9a6c44ee9a89 | -12.00726 | -51.00246 | 2025-09-10 00:30:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 45.9 |


[Clique aqui para ver as próximas entradas](README6.md)
