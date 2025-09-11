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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4d8193b-3992-3681-b2d0-ea69a6e63093 | -13.24686 | -51.77533 | 2025-09-11 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2445b22-026f-3520-b20d-65453dc7398d | -11.88079 | -58.8096 | 2025-09-11 04:23:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 61a6028f-9e9f-3929-a9d7-c709a071b212 | -11.02088 | -45.06686 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b3bae291-0882-38c8-abf8-6880583f5e6b | -11.40678 | -43.5449 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d9fa82a-d240-3e14-adb9-bd9478ad663f | -11.48078 | -49.25436 | 2025-09-11 04:23:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f55ed378-4b9e-3281-90ae-374b6590c76f | -14.38723 | -47.33921 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b626eca3-5c99-3782-8cf5-a6f22cc6b4d9 | -15.22872 | -44.03253 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e04a186-ad02-3340-b1e3-49c13bde95e0 | -11.15702 | -48.35151 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2e305f0-d733-3d32-9876-6d376dd34e6a | -11.47394 | -43.64229 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3f4fc87e-6562-33b8-a876-4bd77d40bffa | -11.31284 | -50.74764 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 08a08f48-9b9b-30b4-bc28-62bef908220c | -11.0181 | -45.06278 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c8ff2fe7-14c0-3373-a16a-5ddc46738642 | -10.39142 | -50.51704 | 2025-09-11 04:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7cd3d56-e101-3aac-9f63-90885fedd690 | -11.40969 | -43.54933 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02f286ba-b870-3f10-9be7-524dfdef60ea | -13.84253 | -47.35523 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f817228-ca0b-391e-b110-3424a8b97647 | -11.81986 | -46.74775 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4bc7040-2ee9-3d3e-bf08-003f4bcf9cd1 | -9.34052 | -48.94204 | 2025-09-11 04:23:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 71a42dd1-63e7-3e96-94ad-aac3be18bbc3 | -12.01579 | -47.58748 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84e24090-1ecf-3527-ae01-f6556eb00f22 | -15.19926 | -44.03627 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5cb4911-7bec-30b0-9256-4b0d6149865d | -13.20382 | -48.3767 | 2025-09-11 04:23:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6138744a-33f0-329d-8acd-61d949700cce | -11.99291 | -47.5989 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f7248769-a471-3670-9815-29b6c0470c42 | -10.5698 | -51.5153 | 2025-09-11 04:23:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01177dbd-77fc-3386-b3d6-527879a1ee32 | -9.02301 | -49.78434 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dba5588c-3f69-3b00-8b4b-9984e54a423d | -11.72276 | -50.639 | 2025-09-11 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 6f4b351b-d84d-33da-803e-c9eba5ed51c0 | -12.06229 | -50.93903 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 321321aa-e4bb-3996-aa11-db422ee692d7 | -9.55087 | -48.24402 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f14764f6-8759-33af-b1e8-78432fcfcab5 | -11.41432 | -43.5421 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a95f51f-ff8f-3225-8cd0-0f04da971b67 | -11.45429 | -43.60778 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 088719dc-ba21-30ba-8e52-f9274ad5cf65 | -8.5235 | -54.76548 | 2025-09-11 04:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b6cb253-cac6-3b91-bf48-bc9892f002f9 | -13.3002 | -43.7527 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 37222b82-cbf3-35ca-9359-7166f17799b4 | -12.94436 | -54.8131 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8ca3229-3f04-3867-89c5-40c4d58a65de | -11.49249 | -43.64817 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86e80095-af4a-32c3-b9ff-b5d7100641e8 | -8.57164 | -51.35173 | 2025-09-11 04:23:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 921f9e2d-e8e5-3679-ac83-15e8816ce940 | -13.65035 | -44.20073 | 2025-09-11 04:23:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17d04a33-1041-358a-ba3e-4acebc992c61 | -11.1671 | -45.27526 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74788468-1822-3745-9d0e-7e4341b067ad | -11.41723 | -43.54652 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 33f79601-3e56-3853-aabc-41f8e0ddd6b3 | -13.85539 | -47.36096 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f12b8745-594a-34ed-ac3f-58c1fd247af9 | -11.68566 | -46.90992 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 756947a6-9db3-3256-a726-cf942d78549d | -14.78674 | -48.22564 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e754d775-35dd-3e95-af2c-eff50e6f4f09 | -11.48902 | -43.64763 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9cad2ca-110a-3585-9c03-d5b3d1831879 | -11.50117 | -43.66139 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd1882e6-1b8c-38aa-957c-fe69f5859c19 | -10.06144 | -50.37457 | 2025-09-11 04:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 714fa45c-bb6f-3cb9-a21c-cbcee7f98fd7 | -9.01357 | -49.52887 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 485a3065-031a-3f60-b5e9-88f5d5bcd35b | -14.3071 | -44.99532 | 2025-09-11 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a61333a9-ea8a-3166-a127-cc18d7a35d3c | -9.38488 | -46.77253 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b868e273-48da-324d-8faf-a8d8fc4e61db | -11.72849 | -46.4729 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d5c04e55-471d-3190-a27c-221f0003c83b | -11.71396 | -50.64271 | 2025-09-11 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fd37c2cf-2406-31a7-92aa-0e758ceceaa5 | -11.4705 | -43.61815 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c9fc2e1-c8f5-3bd2-8fbb-1b94134b23a6 | -8.08021 | -54.74732 | 2025-09-11 04:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3b048dc-7012-3859-bdc8-002f67d16f64 | -12.39666 | -54.16633 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e01cfd4c-a548-3c0a-8da3-af933273aa11 | -11.47397 | -43.61868 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7e67099-70d5-3e16-a815-0e87d0302990 | -14.13366 | -45.40124 | 2025-09-11 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5aed4d06-b1a6-32c5-9c0e-ae833045c808 | -13.16412 | -45.28202 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e356007b-633d-3020-8d85-a316f9e63260 | -12.97428 | -48.04701 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61b75a42-9483-3b11-a466-fb9325794311 | -11.60218 | -52.22032 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36747e84-c48f-3cf5-a4dd-8d7fc6e4ae12 | -9.44847 | -46.42352 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2260a0e7-3fea-3651-a272-5daf6d5e49cf | -13.31796 | -44.64628 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f31253a6-dd1d-34d0-9e05-d7dc48a9580f | -12.13135 | -44.85735 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42596460-6561-3e00-a2e5-060559b5c9bd | -8.80282 | -48.09341 | 2025-09-11 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9124c5a7-57fa-3f76-96e7-643a46fd5eb2 | -11.94505 | -46.64385 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33a1e498-b628-38bd-bb54-c604d8582c17 | -14.39129 | -47.31407 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ac56694-2457-3c92-a36c-6186f72de8d5 | -11.18725 | -48.36407 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 26e0d788-6b9e-34d9-8881-f9b9dc5d1332 | -11.48445 | -43.67842 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 13432195-fc08-3287-90e1-59b491cf0802 | -14.3677 | -47.2993 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| faa8e4a1-b890-3c05-9804-5fb3793dd0c5 | -10.56412 | -43.66344 | 2025-09-11 04:23:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b164adcc-8d23-35ce-9e5e-f3dea9fff31f | -11.36837 | -46.56351 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f74a2cfd-b9a6-3250-ac87-dfa68dd8cb15 | -12.60891 | -56.96224 | 2025-09-11 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91aca95c-7e18-353f-81b5-39695e9d48c4 | -13.97942 | -46.6532 | 2025-09-11 04:23:00 | NPP-375D | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d86c85c1-0c6d-3842-9244-82490a6c55ed | -13.85506 | -43.81905 | 2025-09-11 04:23:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3f89ce34-d624-312c-9cb4-d5431832ac9f | -13.58254 | -47.70618 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71a07c7f-fc0f-3bc6-bb22-6993113c570a | -11.34407 | -46.49041 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ec0f07d5-fb12-384e-89dc-4e7311714ee0 | -11.35124 | -46.50988 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8bf98e15-6356-378f-b636-0121f930a33e | -13.9549 | -48.22604 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3c476671-96eb-39d4-9410-84940d4e03b6 | -8.80997 | -48.09464 | 2025-09-11 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b84c2b5f-0df6-36a1-a12e-d3bf2314c65c | -10.89211 | -47.77078 | 2025-09-11 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8652a8d3-ac42-3e0f-943b-ad490ff9b3f2 | -12.56919 | -44.64146 | 2025-09-11 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2db93be2-c46c-3c56-abbf-eb5bccb37488 | -13.0521 | -47.16492 | 2025-09-11 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0326c118-3390-339c-ac30-522fb2944825 | -13.01222 | -48.72501 | 2025-09-11 04:23:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5c0b27e-76db-36e7-b183-16013ce7c738 | -12.12854 | -44.85319 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4974d2d1-69ce-3d99-922f-91e3492447ad | -15.09597 | -48.04547 | 2025-09-11 04:23:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54f25a87-af0e-3324-be72-6a36c793cfa5 | -11.48208 | -43.64658 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 17235d1b-1ba9-3dd4-83ca-4f47348cd29c | -11.73245 | -50.63017 | 2025-09-11 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5ee57347-d479-302f-864e-56e4cf212f35 | -9.72071 | -43.52554 | 2025-09-11 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bd310680-5c53-3a1a-a704-cea602bcec25 | -11.68025 | -46.87936 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f4e51a8-6403-3046-ad21-8319c24f2655 | -12.02153 | -46.75513 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9a85355-4c1d-382a-aff5-9b23502f4d6a | -13.34509 | -44.00416 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e681fec4-9b36-3098-9c15-0501ca846b23 | -11.16377 | -45.27472 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 828365a0-72ff-3701-96d9-8449003c97cf | -9.45856 | -46.42514 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 5a7809dc-1107-3cbd-b5ea-2c8e68db9a45 | -9.34229 | -48.94426 | 2025-09-11 04:23:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df57e181-9c1f-37a8-b45e-73cfc31aa0ff | -10.57619 | -51.50399 | 2025-09-11 04:23:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5553e8b-7f1f-3277-b813-5948c98a7cf1 | -10.0071 | -51.71718 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c6fceb5-bfe0-3bdd-a195-09441671eded | -12.13697 | -44.86557 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0857aa1f-b10a-30b8-a450-ddac408f3a97 | -11.65822 | -46.90896 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e8d0d1d-98d6-3570-89db-30d660a0c22c | -11.18371 | -48.36351 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64f3e662-b91a-3953-8fc6-601292d7c4fc | -9.02127 | -49.53024 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33983c78-b994-3026-8dab-38ef7e6bf9bc | -9.08144 | -47.07175 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e648c3cb-0d27-39e8-a8fd-727b5d988ac4 | -11.45025 | -43.58741 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dde47652-9343-3998-90a9-ab742ec17c89 | -15.25347 | -44.03641 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d8c5a200-5d19-345e-b4d6-f5600eb397eb | -9.84336 | -47.78006 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e776b4e-b13a-311c-83fb-3689c8e8080e | -11.15271 | -52.03812 | 2025-09-11 04:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c52d4d5-6be7-317a-bcc1-240c718506be | -9.58968 | -48.06698 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README60.md)
